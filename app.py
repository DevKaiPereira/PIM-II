#!/usr/bin/env python3
"""
Interface Gráfica Definitiva - Sistema de Triagem PREX
Conecta-se diretamente à arquitetura modular do PIM-II.
"""

import sys
import os
import platform
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from datetime import datetime
from typing import List

# Garante que a pasta raiz (PIM-II) seja o ponto de partida para os imports
if getattr(sys, 'frozen', False):
    _ROOT_DIR = Path(sys._MEIPASS)
else:
    _ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_ROOT_DIR))

import customtkinter as ctk

# =====================================================================
# IMPORTAÇÕES REAIS DO SEU MOTOR (Baseadas no main.py atual)
# =====================================================================
try:
    from prex_triagem.config.settings import PASTA_RELATORIOS, ARQUIVO_BIBLIOTECA, RELATORIO_CONSOLIDADO
    from prex_triagem.src.pipeline import processar_proposta
    from prex_triagem.src.relatorio import inicializar_csv_consolidado
    from prex_triagem.main import carregar_biblioteca, gerar_pdf_consolidado_a_partir_de_conteudo
    MOTOR_DISPONIVEL = True
except ImportError as e:
    MOTOR_DISPONIVEL = False
    ERRO_IMPORTACAO = str(e)

# Configuração do Tema Visual
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class AppTriagemPREX(ctk.CTk):
    def __init__(self):
        super().__init__()

        if not MOTOR_DISPONIVEL:
            messagebox.showerror("Erro de Arquitetura", f"Não foi possível conectar ao motor PREX.\nErro: {ERRO_IMPORTACAO}")
            self.destroy()
            return

        self.title("🏛️ Sistema de Triagem PREX - PIM II")
        self.geometry("900x650")
        self.minsize(800, 500)

        # Variáveis de Controle
        self.arquivos_selecionados: List[Path] = []
        self.biblioteca_termos = {}
        self.processando = False
        self.ultimo_relatorio_gerado: Path = None

        self._construir_interface()
        self._carregar_dicionario()

    def _construir_interface(self):
        """Monta o layout da janela."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # 1. Cabeçalho
        self.lbl_titulo = ctk.CTkLabel(self, text="Validador Técnico PREX/IFB", font=ctk.CTkFont(size=26, weight="bold"))
        self.lbl_titulo.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

        self.lbl_instrucao = ctk.CTkLabel(
            self, 
            text="Selecione os editais (PDF). O sistema processará as propostas e gerará um PDF final unificado e um CSV.",
            font=ctk.CTkFont(size=14), text_color="gray"
        )
        self.lbl_instrucao.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

        # 2. Painel de Controles
        self.frame_acoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_acoes.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.frame_acoes.grid_columnconfigure(1, weight=1)

        self.btn_buscar = ctk.CTkButton(self.frame_acoes, text="📂 Buscar PDFs", command=self._selecionar_arquivos, font=ctk.CTkFont(weight="bold"))
        self.btn_buscar.grid(row=0, column=0, padx=(0, 15))

        self.lbl_status_arquivos = ctk.CTkLabel(self.frame_acoes, text="Nenhum arquivo na fila.", font=ctk.CTkFont(slant="italic"))
        self.lbl_status_arquivos.grid(row=0, column=1, sticky="w")

        self.btn_iniciar = ctk.CTkButton(
            self.frame_acoes, text="▶ Iniciar Triagem", command=self._iniciar_thread, 
            fg_color="#28a745", hover_color="#218838", font=ctk.CTkFont(weight="bold"), state="disabled"
        )
        self.btn_iniciar.grid(row=0, column=2)

        self.btn_abrir = ctk.CTkButton(
            self.frame_acoes, text="📄 Abrir Relatório", command=self._abrir_relatorio, 
            fg_color="#17a2b8", hover_color="#138496", font=ctk.CTkFont(weight="bold")
        )
        # Nota: btn_abrir é escondido inicialmente, será exibido ao concluir.

        # 3. Terminal Visual (Log)
        self.txt_log = ctk.CTkTextbox(self, state="disabled", font=ctk.CTkFont(family="Consolas", size=13))
        self.txt_log.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

        # 4. Barra de Progresso
        self.frame_prog = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_prog.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.frame_prog.grid_columnconfigure(0, weight=1)

        self.lbl_progresso = ctk.CTkLabel(self.frame_prog, text="Aguardando...")
        self.lbl_progresso.grid(row=0, column=0, sticky="w")
        self.progress_bar = ctk.CTkProgressBar(self.frame_prog)
        self.progress_bar.grid(row=1, column=0, sticky="ew")
        self.progress_bar.set(0)

    def _carregar_dicionario(self):
        """Carrega o JSON de termos do motor."""
        self._escrever_log("Conectando ao motor PREX...")
        try:
            self.biblioteca_termos = carregar_biblioteca(ARQUIVO_BIBLIOTECA)
            self._escrever_log(f"✅ Dicionário carregado com sucesso: {ARQUIVO_BIBLIOTECA.name}")
        except SystemExit:
            self._escrever_log("❌ ERRO CRÍTICO: Arquivo 'biblioteca_termos.json' não encontrado na raiz.")
            self.btn_buscar.configure(state="disabled")

    def _escrever_log(self, texto):
        """Atualiza a caixa de texto de forma segura na thread principal."""
        def atualizar():
            self.txt_log.configure(state="normal")
            hora = datetime.now().strftime("%H:%M:%S")
            self.txt_log.insert(tk.END, f"[{hora}] {texto}\n")
            self.txt_log.see(tk.END)
            self.txt_log.configure(state="disabled")
        self.after(0, atualizar)

    def _selecionar_arquivos(self):
        arquivos = filedialog.askopenfilenames(title="Selecione os PDFs", filetypes=[("Arquivos PDF", "*.pdf")])
        if arquivos:
            self.arquivos_selecionados = [Path(a) for a in arquivos]
            self.lbl_status_arquivos.configure(text=f"{len(self.arquivos_selecionados)} arquivo(s) selecionado(s).")
            self.btn_iniciar.configure(state="normal")
            self._escrever_log(f"📄 {len(self.arquivos_selecionados)} PDFs prontos para análise.")

    def _iniciar_thread(self):
        if not self.arquivos_selecionados or self.processando:
            return
        self.processando = True
        self.btn_buscar.configure(state="disabled")
        self.btn_iniciar.configure(state="disabled")
        self.btn_abrir.grid_remove() # Oculta o botão na nova remessa
        self.ultimo_relatorio_gerado = None
        
        self.txt_log.configure(state="normal")
        self.txt_log.delete("1.0", tk.END)
        self.txt_log.configure(state="disabled")
        
        threading.Thread(target=self._executar_pipeline, daemon=True).start()

    def _executar_pipeline(self):
        total = len(self.arquivos_selecionados)
        todos_conteudos_relatorios = []
        
        self._escrever_log("="*50)
        self._escrever_log("🚀 INICIANDO TRIAGEM")
        self._escrever_log("="*50)

        # Inicializa o CSV (igual ao main.py)
        inicializar_csv_consolidado(RELATORIO_CONSOLIDADO)

        for i, caminho_pdf in enumerate(self.arquivos_selecionados, start=1):
            self._escrever_log(f"Analisando [{i}/{total}]: {caminho_pdf.name}...")
            try:
                # Chama exatamente a mesma função que o seu main.py chama
                resultado = processar_proposta(
                    caminho_pdf=caminho_pdf,
                    biblioteca=self.biblioteca_termos,
                    caminho_csv_consolidado=RELATORIO_CONSOLIDADO
                )
                
                if resultado and resultado.get("report_content"):
                    todos_conteudos_relatorios.append(resultado["report_content"])
                    self._escrever_log(f"  ✅ Concluído.")
                else:
                    self._escrever_log(f"  ⚠️ Processado, mas sem conteúdo gerado.")
            except Exception as e:
                self._escrever_log(f"  ❌ Erro ao processar: {e}")

            # Atualiza Barra de Progresso
            percentual = i / total
            self.after(0, lambda p=percentual, at=i, tt=total: self._atualizar_progresso(p, at, tt))

        # Fase Final: Geração do PDF Consolidado
        self._escrever_log("="*50)
        if todos_conteudos_relatorios:
            self._escrever_log("🖨️ Empacotando resultados em PDF único...")
            
            nome_consolidado = f"relatorio_consolidado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)
            caminho_saida = PASTA_RELATORIOS / nome_consolidado
            
            caminho_gerado = gerar_pdf_consolidado_a_partir_de_conteudo(todos_conteudos_relatorios, caminho_saida)
            
            if caminho_gerado:
                self.ultimo_relatorio_gerado = caminho_gerado.resolve()
                self._escrever_log(f"✅ PDF CONSOLIDADO SALVO EM: {self.ultimo_relatorio_gerado}")
                self.after(0, lambda: messagebox.showinfo("Sucesso!", f"Triagem concluída!\nO relatório foi salvo em:\n\n{self.ultimo_relatorio_gerado}"))
            else:
                self._escrever_log("❌ Falha na biblioteca reportlab. PDF não gerado.")
        else:
            self._escrever_log("⚠️ Nenhum conteúdo válido extraído. PDF cancelado.")

        # Restaura a interface
        self.after(0, self._restaurar_interface)

    def _atualizar_progresso(self, percentual, atual, total):
        self.progress_bar.set(percentual)
        self.lbl_progresso.configure(text=f"Progresso: {atual} de {total} ( {int(percentual*100)}% )")

    def _restaurar_interface(self):
        self.processando = False
        self.btn_buscar.configure(state="normal")
        self.btn_iniciar.configure(state="normal")
        
        if self.ultimo_relatorio_gerado:
            self._escrever_log("🗂️ Clique no botão 'Abrir Relatório' acima para visualizá-log agora.")
            self.btn_abrir.grid(row=0, column=3, padx=(15, 0))
        else:
            self._escrever_log("🏁 Aguardando nova remessa de arquivos.")

    def _abrir_relatorio(self):
        if self.ultimo_relatorio_gerado and self.ultimo_relatorio_gerado.exists():
            try:
                caminho_str = str(self.ultimo_relatorio_gerado)
                if platform.system() == 'Windows':
                    os.startfile(caminho_str)
                elif platform.system() == 'Darwin':
                    subprocess.call(('open', caminho_str))
                else:
                    subprocess.call(('xdg-open', caminho_str))
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo.\n{e}")
        else:
            messagebox.showwarning("Aviso", "O relatório não foi encontrado.")

if __name__ == "__main__":
    app = AppTriagemPREX()
    app.mainloop()