import logging
from pathlib import Path
from typing import Any, Optional

from prex_triagem.src.extrator import preparar_documento
from prex_triagem.src.validador import validar_todos_os_pilares
from prex_triagem.src.pontuador import calcular_pontuacao_merito
from prex_triagem.src.relatorio import (
    gerar_relatorio_individual,
    registrar_no_csv_consolidado,
)

logger = logging.getLogger(__name__)


def processar_proposta(
    caminho_pdf: Path,
    biblioteca: dict[str, Any],
    caminho_csv_consolidado: Path,
) -> Optional[dict[str, Any]]:
 
    nome_arquivo = caminho_pdf.name
    logger.info(">>> Iniciando triagem: %s", nome_arquivo)

    texto_normalizado = preparar_documento(caminho_pdf)

    if not texto_normalizado:
        logger.error(
            "Não foi possível extrair texto de '%s'. Proposta ignorada.",
            nome_arquivo
        )
        return None

    if len(texto_normalizado) < 100:
        logger.warning(
            "'%s' possui texto muito curto (%d chars). "
            "Pode ser um PDF escaneado sem OCR.",
            nome_arquivo, len(texto_normalizado)
        )

    resultados_blocos = validar_todos_os_pilares(
        texto_normalizado, biblioteca
    )

    config_bloco5 = biblioteca.get("bloco_5_merito", {})
    resultado_merito = calcular_pontuacao_merito(texto_normalizado, config_bloco5)

    report_content = gerar_relatorio_individual(
        nome_arquivo=nome_arquivo,
        resultados_blocos=resultados_blocos,
        resultado_merito=resultado_merito
    )

    registrar_no_csv_consolidado(
        caminho_csv=caminho_csv_consolidado,
        nome_arquivo=nome_arquivo,
        resultados_blocos=resultados_blocos,
        resultado_merito=resultado_merito,
    )

    print(
        f"  ✅ Concluído | Mérito: {resultado_merito['pontuacao_total']:>3}pts "
        f"({resultado_merito['classificacao']}) | "
        f"{nome_arquivo}"
    )
    logger.info(
        "<<< Triagem concluída: %s | Mérito: %d pts",
        nome_arquivo, resultado_merito["pontuacao_total"]
    )

    return {
        "arquivo": nome_arquivo,
        "pontuacao_merito": resultado_merito["pontuacao_total"],
        "classificacao_merito": resultado_merito["classificacao"],
        "report_content": report_content,
    }