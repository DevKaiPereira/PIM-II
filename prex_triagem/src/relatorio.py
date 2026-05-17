import csv
import logging
import textwrap
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    REPORTLAB_DISPONIVEL = True
except ImportError:  
    REPORTLAB_DISPONIVEL = False

SEPARADOR = "=" * 70
SEPARADOR_FINO = "-" * 70

NOMES_BLOCOS = {
    "P1": "Pilar 1 — Admissibilidade e Vínculo",
    "P2": "Pilar 2 — Configuração de Equipe",
    "P3": "Pilar 3 — Dimensão Pedagógica",
    "P4": "Pilar 4 — Enquadramento Estratégico",
    "P5": "Pilar 5 — Recursos e Viabilidade",
    "P6": "Pilar 6 — Conformidade Documental",
}

logger = logging.getLogger(__name__)

def gerar_relatorio_individual(
    nome_arquivo: str,
    resultados_blocos: dict[str, Any],
    resultado_merito: dict[str, Any],
    pasta_saida: Path,
) -> list[str]:

    status = determinar_status(resultados_blocos, resultado_merito) # Mantido apenas para logs internos
    pasta_saida_pdf: Path | None = None,
) -> Path:

    agora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    nome_relatorio = f"{Path(nome_arquivo).stem}_relatorio.txt"
    caminho_saida = pasta_saida / nome_relatorio

    linhas = []
    
    # Pega a classificação de mérito para brilhar no topo
    classificacao_merito = resultado_merito.get('classificacao', 'NÃO AVALIADO').upper()

    linhas += [
        SEPARADOR,
        "  PARECER CONSULTIVO DA MÁQUINA — PREX/IFB",
        "  Base legal: Resolução nº 42/2020",
        SEPARADOR,
        f"  Proposta analisada  : {nome_arquivo}",
        f"  Data/hora da análise: {agora}",
        SEPARADOR,
        f"  CLASSIFICAÇÃO DE MÉRITO: {classificacao_merito} 🌟",
        SEPARADOR,
        "",
    ]

    # --- NOVO PAINEL INTELIGENTE DE ATENÇÃO PARA A EQUIPE ---
    avisos_topo = []
    for chave_bloco, nome_bloco in NOMES_BLOCOS.items():
        resultado = resultados_blocos.get(chave_bloco, {})
        for imp in resultado.get("impedimentos", []):
            avisos_topo.append(f"- A máquina detectou a palavra '{imp}' no {nome_bloco}. Requer leitura humana rápida para confirmar contexto.")
        for alerta in resultado.get("alertas", []):
            avisos_topo.append(f"- Alerta no {nome_bloco}: {alerta}")

    if avisos_topo:
        linhas.append("  ATENÇÃO DA EQUIPE DE AVALIAÇÃO:")
        for aviso in avisos_topo:
            linhas.append(f"  {aviso}")
    else:
        linhas.append("  ATENÇÃO DA EQUIPE: A máquina não detectou palavras impeditivas. Documentação base parece regular.")
    
    linhas.append(SEPARADOR_FINO)
    linhas.append("")
    linhas.append("  DETALHAMENTO DA VARREDURA TÉCNICA:")
    linhas.append("")

    # --- RENDERIZAÇÃO DOS BLOCOS (Mantida igual ao original) ---
    for chave_bloco, nome_bloco in NOMES_BLOCOS.items():
        resultado = resultados_blocos.get(chave_bloco, {})
        aprovado = resultado.get("aprovado", False)
        # O ícone muda para um aviso se tiver impedimentos, mas não diz mais "Reprovado"
        icone = "✅" if aprovado else "⚠️"

        linhas += [
            f"{icone}  {nome_bloco}",
            SEPARADOR_FINO,
        ]

        encontrados = resultado.get("termos_encontrados", [])
        if encontrados:
            linhas.append(f"   Termos encontrados  : {', '.join(encontrados)}")
        else:
            linhas.append("   Termos encontrados  : (nenhum)")

        ausentes = resultado.get("termos_ausentes", [])
        if ausentes:
            linhas.append(f"   Termos ausentes     : {', '.join(ausentes)}")

        for alerta in resultado.get("alertas", []):
            linhas.append(f"   ⚠️  Alerta            : {alerta}")

        for imp in resultado.get("impedimentos", []):
            linhas.append(f"   🛑 Termo Impeditivo  : {imp}")

        linhas.append("")

    # --- RENDERIZAÇÃO DO MÉRITO (Detalhes) ---
    linhas += [
        "📊  Avaliação de Mérito e Qualidade",
        SEPARADOR_FINO,
        f"   Pontuação obtida    : {resultado_merito.get('pontuacao_total', 0)} / "
        f"{resultado_merito.get('pontuacao_maxima', 42)} pontos",
        "",
        "   Detalhamento por categoria:",
    ]

    for categoria, detalhe in resultado_merito.get("detalhes_categorias", {}).items():
        nome_cat = categoria.replace("_", " ").title()
        pontos = detalhe.get("pontos_obtidos", 0)
        maximo = detalhe.get("max_pontos", 0)
        termos_cat = [t["termo"] for t in detalhe.get("termos_encontrados", [])]
        termos_str = ", ".join(termos_cat) if termos_cat else "—"
        linhas.append(
            f"     • {nome_cat:<25} {pontos:>2}/{maximo:<2} pts  |  "
            f"Termos: {termos_str}"
        )

    linhas += [
        "",
        SEPARADOR,
        "  ⚠️  AVISO: Este relatório é uma ferramenta de APOIO à triagem.",
        "  A decisão final de admissibilidade é humana, de responsabilidade da PREX/IFB.",
        SEPARADOR,
    ]

    logger.debug("Conteúdo do relatório individual gerado para '%s'.", nome_arquivo)
    return linhas
    pasta_saida.mkdir(parents=True, exist_ok=True)
    caminho_saida.write_text("\n".join(linhas), encoding="utf-8")

    pasta_pdf = pasta_saida_pdf or pasta_saida
    pasta_pdf.mkdir(parents=True, exist_ok=True)
    caminho_pdf = pasta_pdf / f"{Path(nome_arquivo).stem}_relatorio.pdf"
    pdf_ok = _gerar_pdf_relatorio(linhas, caminho_pdf)

    logger.info("Relatório individual gerado: %s", caminho_saida)
    if pdf_ok:
        logger.info("Relatório PDF gerado: %s", caminho_pdf)
    return caminho_saida

def inicializar_csv_consolidado(caminho_csv: Path) -> None:

    caminho_csv.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "arquivo",
            "status",
            "p1_aprovado",
            "p1_impedimentos",
            "p2_aprovado",
            "p2_alertas",
            "p3_aprovado",
            "p3_impedimentos",
            "p4_aprovado",
            "p4_alertas",
            "p5_aprovado",
            "p5_alertas",
            "p6_aprovado",
            "p6_impedimentos",
            "bloco1_aprovado",
            "bloco1_impedimentos",
            "bloco2_aprovado",
            "bloco2_alertas",
            "bloco3_aprovado",
            "bloco3_impedimentos",
            "bloco4_aprovado",
            "bloco4_alertas",
            "pontuacao_merito",
            "classificacao_merito",
            "data_analise",
        ])
    logger.info("CSV consolidado inicializado: %s", caminho_csv)


def registrar_no_csv_consolidado(
    caminho_csv: Path,
    nome_arquivo: str,
    resultados_blocos: dict[str, Any],
    resultado_merito: dict[str, Any],
) -> None:

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def _imp(bloco_key: str) -> str:
        imps = resultados_blocos.get(bloco_key, {}).get("impedimentos", [])
        return " | ".join(imps) if imps else ""

    def _ale(bloco_key: str) -> str:
        ales = resultados_blocos.get(bloco_key, {}).get("alertas", [])
        return " | ".join(ales) if ales else ""

    linha = [
        nome_arquivo,
        status,
        resultados_blocos.get("P1", {}).get("aprovado", False),
        _imp("P1"),
        resultados_blocos.get("P2", {}).get("aprovado", False),
        _ale("P2"),
        resultados_blocos.get("P3", {}).get("aprovado", False),
        _imp("P3"),
        resultados_blocos.get("P4", {}).get("aprovado", False),
        _ale("P4"),
        resultados_blocos.get("P5", {}).get("aprovado", False),
        _ale("P5"),
        resultados_blocos.get("P6", {}).get("aprovado", False),
        _imp("P6"),
        resultados_blocos.get("bloco_1", {}).get("aprovado", False),
        _imp("bloco_1"),
        resultados_blocos.get("bloco_2", {}).get("aprovado", False),
        _ale("bloco_2"),
        resultados_blocos.get("bloco_3", {}).get("aprovado", False),
        _imp("bloco_3"),
        resultados_blocos.get("bloco_4", {}).get("aprovado", False),
        _ale("bloco_4"),
        resultado_merito.get("pontuacao_total", 0),
        resultado_merito.get("classificacao", ""),
        agora,
    ]

    with open(caminho_csv, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(linha)

    logger.debug("Registrado no CSV: %s", nome_arquivo)