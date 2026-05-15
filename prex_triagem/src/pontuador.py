import logging
import re
from typing import Any

from prex_triagem.src.extrator import normalizar_texto

logger = logging.getLogger(__name__)


def _normalizar_termo(termo: str) -> str:
    return normalizar_texto(termo)


def _compilar_padrao_termo(termo: str) -> re.Pattern[str] | None:
    
    termo_norm = _normalizar_termo(termo)
    if not termo_norm:
        return None

    partes = termo_norm.split()
    if not partes:
        return None

    if len(partes) == 1:
        nucleo = re.escape(partes[0])
    else:
        separador = r"(?:[\W_]+)"
        nucleo = separador.join(re.escape(p) for p in partes)

    padrao = rf"(?<!\w){nucleo}(?!\w)"
    return re.compile(padrao)


def _contar_ocorrencias(texto: str, termo: str) -> int:
    padrao = _compilar_padrao_termo(termo)
    if padrao is None:
        return 0
    return len(padrao.findall(texto))


def calcular_pontuacao_merito(
    texto: str, config_bloco5: dict[str, Any]
) -> dict[str, Any]:

    texto = normalizar_texto(texto)

    termos_merito = config_bloco5.get("termos_de_merito", {})
    limiares = config_bloco5.get("limiares", {})
    pontuacao_maxima = config_bloco5.get("pontuacao_maxima_total")

    pontuacao_total = 0
    detalhes = {}

    for nome_categoria, config_cat in termos_merito.items():
        termos = config_cat.get("termos", [])
        pontos_por_ocorrencia = config_cat.get("pontos_por_ocorrencia", 1)
        max_pontos = config_cat.get("max_pontos", 10)

        pontos_categoria = 0
        termos_encontrados_cat = []

        for termo in termos:
            ocorrencias = _contar_ocorrencias(texto, termo)
            if ocorrencias > 0:
                pontos_brutos = ocorrencias * pontos_por_ocorrencia
                termos_encontrados_cat.append({
                    "termo": termo,
                    "ocorrencias": ocorrencias,
                    "pontos_brutos": pontos_brutos,
                })
                pontos_categoria += pontos_brutos

        pontos_categoria = min(pontos_categoria, max_pontos)
        pontuacao_total += pontos_categoria

        detalhes[nome_categoria] = {
            "pontos_obtidos": pontos_categoria,
            "max_pontos": max_pontos,
            "termos_encontrados": termos_encontrados_cat,
        }

        logger.debug(
            "Mérito — categoria '%s': %d/%d pontos | Termos: %s",
            nome_categoria,
            pontos_categoria,
            max_pontos,
            [t["termo"] for t in termos_encontrados_cat],
        )

    if pontuacao_maxima is None:
        pontuacao_maxima = sum(
            int(cat.get("max_pontos", 0))
            for cat in termos_merito.values()
            if isinstance(cat, dict)
        )

    limiar_alto = limiares.get("alto_merito", 25)
    limiar_medio = limiares.get("medio_merito", 12)

    if pontuacao_total >= limiar_alto:
        classificacao = "Alto Mérito"
    elif pontuacao_total >= limiar_medio:
        classificacao = "Médio Mérito"
    else:
        classificacao = "Baixo Mérito"

    logger.info(
        "Pontuação de mérito: %d/%d — %s",
        pontuacao_total, pontuacao_maxima, classificacao
    )

    return {
        "pontuacao_total": pontuacao_total,
        "pontuacao_maxima": pontuacao_maxima,
        "classificacao": classificacao,
        "detalhes_categorias": detalhes,
    }


def avaliar_status_burocratico(**aprovacoes: bool) -> dict[str, Any]:
  
    nome_map = {
        "bloco1": "Bloco 1 - Exercício Pleno",
        "bloco2": "Bloco 2 - Vínculo Institucional",
        "bloco3": "Bloco 3 - Composição da Equipe",
        "bloco4": "Bloco 4 - Aderência ao Edital",
    }

    falhas = [nome_map.get(k, k) for k, v in aprovacoes.items() if not v]
    status = "APTO" if not falhas else "INAPTO"

    logger.info("Avaliação burocrática: %s. Falhas: %s", status, falhas)

    return {"status": status, "falhas": falhas}
