import logging
import re
from typing import Any, List, Dict

logger = logging.getLogger(__name__)

def _encontrar_termos(texto: str, lista_termos: List[str]) -> List[str]:
    """
    Retorna quais termos da lista foram encontrados no texto.
    A busca é feita como palavra inteira (case insensitive).
    """
    encontrados = []
    texto_lower = texto.lower()
    for termo in lista_termos:
        padrao = r"\b" + re.escape(termo.lower()) + r"\b"
        if re.search(padrao, texto_lower):
            encontrados.append(termo)
    return encontrados


def validar_pilar(texto: str, pilar: Dict[str, Any]) -> Dict[str, Any]:
    """
    Avalia um pilar completo da biblioteca, processando seus processos e conceitos.
    Retorna um dicionário com status de aprovação, termos encontrados/ausentes,
    impedimentos e alertas.
    """
    resultado = {
        "aprovado": False,
        "termos_encontrados": [],
        "termos_ausentes": [],
        "alertas": [],
        "impedimentos": [],
    }

    todos_encontrados = []
    todos_ausentes = []

    for proc in pilar.get("processes", []):
        for concept in proc.get("concepts", []):
            termo_principal = concept.get("termo_principal", "")
            sinonimos = concept.get("sinonimos", [])
            contexto_obrigatorio = concept.get("contexto_obrigatorio", [])
            contexto_negacao = concept.get("contexto_negacao", [])

            # Lista de busca: termo principal + todos os sinônimos
            termos_busca = [termo_principal] + sinonimos
            encontrados = _encontrar_termos(texto, termos_busca)

            if encontrados:
                todos_encontrados.extend(encontrados)

                # 1. Verificar termos de negação → impedimento imediato
                if contexto_negacao:
                    impedimentos = _encontrar_termos(texto, contexto_negacao)
                    if impedimentos:
                        resultado["impedimentos"].extend(impedimentos)
                        logger.warning(
                            "Pilar '%s' — Impedimento detectado no conceito '%s': %s",
                            pilar.get("name"),
                            termo_principal,
                            impedimentos,
                        )

                # 2. Verificar se os contextos obrigatórios aparecem
                if contexto_obrigatorio:
                    obrigatorios = _encontrar_termos(texto, contexto_obrigatorio)
                    if not obrigatorios:
                        resultado["alertas"].append(
                            f"Conceito '{termo_principal}' encontrado, mas sem contexto obrigatório na proposta."
                        )
            else:
                todos_ausentes.append(termo_principal)

    # Consolidação e ordenação
    resultado["termos_encontrados"] = sorted(list(set(todos_encontrados)))
    resultado["termos_ausentes"] = sorted(list(set(todos_ausentes)))
    resultado["impedimentos"] = sorted(list(set(resultado["impedimentos"])))
    resultado["alertas"] = sorted(list(set(resultado["alertas"])))

    # Decisão final para o pilar
    if resultado["impedimentos"]:
        resultado["aprovado"] = False
    elif todos_encontrados:
        resultado["aprovado"] = True
    else:
        resultado["aprovado"] = False
        resultado["alertas"].append("Nenhum termo relevante encontrado para este pilar.")

    return resultado


def validar_todos_os_pilares(
    texto: str,
    biblioteca: Dict[str, Any],
) -> Dict[str, Dict[str, Any]]:
    """
    Percorre todos os pilares da biblioteca e retorna um dicionário
    com o resultado da validação de cada um.

    Retorno:
        {
            "P1": { "aprovado": bool, "termos_encontrados": [...], ... },
            "P2": { ... },
            ...
        }
    """
    resultados = {}

    pillars = biblioteca.get("pillars", [])
    if not pillars:
        logger.warning("Biblioteca de validação não contém pilares.")

    for pilar in pillars:
        pid = pilar.get("id")
        if not pid:
            logger.warning("Pilar sem 'id' ignorado: %s", pilar.get("name", "desconhecido"))
            continue
        resultados[pid] = validar_pilar(texto, pilar)

    return resultados