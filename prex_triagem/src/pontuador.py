import logging
import re
from typing import Any

logger = logging.getLogger(__name__)


def _contar_ocorrencias(texto: str, termo: str) -> int:

    padrao = r"\b" + re.escape(termo) + r"\b"
    return len(re.findall(padrao, texto))


def calcular_pontuacao_merito(
    texto: str, config_bloco5: dict[str, Any]
) -> dict[str, Any]:
  
    termos_merito = config_bloco5.get("termos_de_merito", {})
    limiares = config_bloco5.get("limiares", {})
    pontuacao_maxima = config_bloco5.get("pontuacao_maxima_total", 42)

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
    """Avalia os quatro portões burocráticos e retorna status e motivos.

    Uso sugerido:
      resultado = avaliar_status_burocratico(
          bloco1=aprovado_b1,
          bloco2=aprovado_b2,
          bloco3=aprovado_b3,
          bloco4=aprovado_b4,
      )

    Retorna dicionário com 'status' = 'APTO'|'INAPTO' e 'falhas' = lista de blocos reprovados.
    """
    # Normalizar nomes dos blocos para mensagens legíveis
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
