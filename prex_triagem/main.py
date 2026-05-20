import json
import logging
import sys
from datetime import datetime
from pathlib import Path
import unicodedata
import textwrap
from typing import List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

from config.settings import (
    PASTA_PDFS,
    PASTA_RELATORIOS,
    ARQUIVO_BIBLIOTECA,
    RELATORIO_CONSOLIDADO,
    # ARQUIVO_LOG, # Removed from here, defined globally below
    # EXTENSOES_ACEITAS, # Removed from here, defined globally below
    # VERBOSE, # Removed from here, defined globally below
    ARQUIVO_LOG,
    EXTENSOES_ACEITAS,
    VERBOSE,
)
from prex_triagem.src.pipeline import processar_proposta
from prex_triagem.src.relatorio import inicializar_csv_consolidado # Keep this for CSV

# Importar reportlab para consolidar PDFs
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    REPORTLAB_DISPONIVEL = True
except ImportError:
    REPORTLAB_DISPONIVEL = False

def configurar_logging(nivel_console: int = logging.INFO) -> None:

    ARQUIVO_LOG.parent.mkdir(parents=True, exist_ok=True)

    formato = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    data_formato = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=logging.DEBUG,  
        format=formato,
        datefmt=data_formato,
        handlers=[
            logging.FileHandler(ARQUIVO_LOG, encoding="utf-8", mode="a"),
            logging.StreamHandler(sys.stdout),
        ],
    )

    logging.getLogger().handlers[1].setLevel(
        logging.DEBUG if VERBOSE else nivel_console
    )

    logging.getLogger("pdfminer").setLevel(logging.WARNING)
    logging.getLogger("pdfplumber").setLevel(logging.WARNING)
    logging.getLogger("PyPDF2").setLevel(logging.WARNING)
    
logger = logging.getLogger(__name__)

def carregar_biblioteca(caminho: Path) -> dict:

    if not caminho.exists():
        logging.critical(
            "Arquivo de biblioteca não encontrado: %s\n"
            "Verifique se 'biblioteca_termos.json' está na raiz do projeto.",
            caminho
        )
        sys.exit(1)

    try:
        with open(caminho, encoding="utf-8") as f:
            dados = json.load(f)
        logging.info("Biblioteca carregada: %s", caminho)
        return dados
    except json.JSONDecodeError as erro:
        logging.critical(
            "Erro ao ler '%s': JSON inválido.\nDetalhe: %s", caminho, erro
        )
        sys.exit(1)

def listar_pdfs(pasta: Path) -> list[Path]:

    if not pasta.exists():
        pasta.mkdir(parents=True, exist_ok=True)
        logging.warning(
            "Pasta de PDFs não encontrada: %s\n"
            "A pasta foi criada automaticamente. Adicione os PDFs nela e execute o programa novamente.",
            pasta
        )
        return []

    pdfs = sorted([
        arq for arq in pasta.iterdir()
        if arq.suffix.lower() in EXTENSOES_ACEITAS
    ])

    logging.info("PDFs encontrados em '%s': %d arquivo(s).", pasta, len(pdfs))
    return pdfs

def gerar_pdf_consolidado_a_partir_de_conteudo(
    todos_conteudos_relatorios: List[List[str]], caminho_saida: Path
) -> Optional[Path]:
    """
    Gera um único PDF a partir de uma lista de conteúdos de relatórios (listas de strings).
    """
    if not REPORTLAB_DISPONIVEL:
        logger.error("reportlab não está instalado. Não é possível gerar o PDF consolidado.")
        return None

    if not todos_conteudos_relatorios:
        logger.info("Nenhum conteúdo de relatório para consolidar.")
        return None
    try:
        caminho_saida.parent.mkdir(parents=True, exist_ok=True)

        pagina_largura, pagina_altura = A4
        margem = 0.5 * inch
        fonte = "Courier"
        tamanho_fonte = 9
        altura_linha = tamanho_fonte + 2
        largura_wrap = int((pagina_largura - 2 * margem) / (tamanho_fonte * 0.6))

        c = canvas.Canvas(str(caminho_saida), pagesize=A4)
        c.setFont(fonte, tamanho_fonte)

        for i, linhas_relatorio in enumerate(todos_conteudos_relatorios):
            if i > 0:
                c.showPage()
                c.setFont(fonte, tamanho_fonte)
            
            y = pagina_altura - margem

            for linha in linhas_relatorio:
                linha_sanitizada = unicodedata.normalize("NFKD", linha).encode("ascii", "ignore").decode("ascii")
                partes = textwrap.wrap(linha_sanitizada, width=largura_wrap) or [""]

                for parte in partes:
                    if y < margem:
                        c.showPage()
                        c.setFont(fonte, tamanho_fonte)
                        y = pagina_altura - margem

                    c.drawString(margem, y, parte)
                    y -= altura_linha

        c.save()
        logger.info("PDF consolidado gerado em: %s", caminho_saida.resolve())
        return caminho_saida
    except Exception as e:
        logger.error("Erro ao salvar o PDF consolidado em '%s': %s", caminho_saida, e)
        return None

def exibir_resumo_final(resultados: list[dict], caminho_pdf_consolidado: Optional[Path] = None) -> None:

    total = len(resultados)

    print("\n" + "=" * 70)
    print("  RESUMO — TRIAGEM PREX")
    print("=" * 70)
    print(f"  Total de propostas analisadas : {total}")
    print("=" * 70)

    if caminho_pdf_consolidado:
        print(f"\n  📦 PDF Consolidado de Relatórios: {caminho_pdf_consolidado.resolve()}")
    print(f"   Relatório consolidado (CSV): {RELATORIO_CONSOLIDADO}")
    print(f"  📝 Log completo: {ARQUIVO_LOG}")
    print("=" * 70)

def main() -> None:

    configurar_logging()
    logger = logging.getLogger(__name__)

    inicio = datetime.now()
    logger.info("=" * 60)
    logger.info("INÍCIO DA TRIAGEM — %s", inicio.strftime("%d/%m/%Y %H:%M:%S"))
    logger.info("=" * 60)

    print("\n" + "=" * 70)
    print("  🏛️  TRIAGEM PREX")
    print(f"  Base legal: Resolução nº 42/2020")
    print(f"  Execução: {inicio.strftime('%d/%m/%Y às %H:%M')}")
    print("=" * 70)

    biblioteca = carregar_biblioteca(ARQUIVO_BIBLIOTECA)

    pdfs = listar_pdfs(PASTA_PDFS)

    if not pdfs:
        print(
            f"\n  ⚠️  Nenhum PDF encontrado em '{PASTA_PDFS}'.\n"
            "  Adicione os arquivos e execute novamente.\n"
        )
        return

    print(f"\n  📂 {len(pdfs)} proposta(s) encontrada(s). Iniciando triagem...\n")
    print("-" * 70)

    PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)
    inicializar_csv_consolidado(RELATORIO_CONSOLIDADO)

    resultados = []
    todos_conteudos_relatorios: List[List[str]] = []
    for indice, caminho_pdf in enumerate(pdfs, start=1):
        print(f"  [{indice:>3}/{len(pdfs)}] Analisando: {caminho_pdf.name}")

        resultado = processar_proposta(
            caminho_pdf=caminho_pdf,
            biblioteca=biblioteca,
            caminho_csv_consolidado=RELATORIO_CONSOLIDADO,
        )

        if resultado:
            if resultado.get("report_content"):
                todos_conteudos_relatorios.append(resultado["report_content"])
            resultados.append(resultado)

    fim = datetime.now()
    duracao = (fim - inicio).total_seconds()

    logger.info(
        "TRIAGEM CONCLUÍDA em %.1f segundos. %d/%d propostas processadas.",
        duracao, len(resultados), len(pdfs)
    )
    
    # Consolidar todos os PDFs individuais em um único arquivo
    caminho_pdf_consolidado = None
    if todos_conteudos_relatorios:
        nome_consolidado = f"relatorio_consolidado_{fim.strftime('%Y%m%d_%H%M%S')}.pdf"
        caminho_pdf_consolidado = PASTA_RELATORIOS / nome_consolidado
        caminho_pdf_consolidado = gerar_pdf_consolidado_a_partir_de_conteudo(todos_conteudos_relatorios, caminho_pdf_consolidado)

    exibir_resumo_final(resultados, caminho_pdf_consolidado)
    
    print(f"\n  ⏱️  Tempo total: {duracao:.1f} segundos\n")


if __name__ == "__main__":
    main()