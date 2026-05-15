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
except ImportError:  # pragma: no cover
    REPORTLAB_DISPONIVEL = False

SEPARADOR = "=" * 70
SEPARADOR_FINO = "-" * 70

ICONE_STATUS = {
    "APTO": "✅ APTO",
    "ALERTA": "⚠️  ALERTA",
    "INAPTO": "❌ INAPTO",
}

NOMES_BLOCOS = {
    "bloco_1": "Bloco 1 — Exercício Pleno",
    "bloco_2": "Bloco 2 — Vínculo Institucional",
    "bloco_3": "Bloco 3 — Composição da Equipe",
    "bloco_4": "Bloco 4 — Aderência ao Edital",
}


def _sanitizar_texto_para_pdf(texto: str) -> str:
    if not texto:
        return ""
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode("ascii")
    return texto


def _gerar_pdf_relatorio(linhas: list[str], caminho_pdf: Path) -> bool:
    if not REPORTLAB_DISPONIVEL:
        logger.warning(
            "reportlab não instalado; pulando geração de PDF (%s)",
            caminho_pdf.name,
        )
        return False

    pagina_largura, pagina_altura = A4
    margem = 36  # 0.5 in
    fonte = "Courier"
    tamanho_fonte = 9
    altura_linha = tamanho_fonte + 2

    c = canvas.Canvas(str(caminho_pdf), pagesize=A4)
    c.setFont(fonte, tamanho_fonte)

    y = pagina_altura - margem

    largura_wrap = 110

    for linha in linhas:
        linha = _sanitizar_texto_para_pdf(linha)
        partes = textwrap.wrap(linha, width=largura_wrap) or [""]

        for parte in partes:
            if y < margem:
                c.showPage()
                c.setFont(fonte, tamanho_fonte)
                y = pagina_altura - margem

            c.drawString(margem, y, parte)
            y -= altura_linha

    c.save()
    return True

def determinar_status(
    resultados_blocos: dict[str, Any],
    resultado_merito: dict[str, Any],
) -> str:

    for nome_bloco, resultado in resultados_blocos.items():
        if resultado.get("impedimentos"):
            return "INAPTO"

    for nome_bloco, resultado in resultados_blocos.items():
        if not resultado.get("aprovado", False):
            return "ALERTA"

    return "APTO"

def gerar_relatorio_individual(
    nome_arquivo: str,
    resultados_blocos: dict[str, Any],
    resultado_merito: dict[str, Any],
    pasta_saida: Path,
) -> Path:

    status = determinar_status(resultados_blocos, resultado_merito) # Mantido apenas para logs internos
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
        "📊  Bloco 5 — Mérito e Qualidade",
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

    pasta_saida.mkdir(parents=True, exist_ok=True)
    caminho_saida.write_text("\n".join(linhas), encoding="utf-8")

    caminho_pdf = caminho_saida.with_suffix(".pdf")
    pdf_ok = _gerar_pdf_relatorio(linhas, caminho_pdf)

    logger.info(
        "Relatório individual gerado: %s (Status Interno: %s)", caminho_saida, status
    )
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

    status = determinar_status(resultados_blocos, resultado_merito)
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

    logger.debug("Registrado no CSV: %s — %s", nome_arquivo, status)