import logging
import re
from typing import Any

logger = logging.getLogger(__name__)

def _encontrar_termos(texto: str, lista_termos: list[str]) -> list[str]:

    encontrados = []
    texto_lower = texto.lower()
    for termo in lista_termos:
        padrao = r"\b" + re.escape(termo.lower()) + r"\b"
        if re.search(padrao, texto_lower):
            encontrados.append(termo)
    return encontrados

def validar_pilar(texto: str, pilar: dict[str, Any]) -> dict[str, Any]:
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

            termos_busca = [termo_principal] + sinonimos
            encontrados = _encontrar_termos(texto, termos_busca)

            if encontrados:
                todos_encontrados.extend(encontrados)

                if contexto_negacao:
                    impedimentos = _encontrar_termos(texto, contexto_negacao)
                    if impedimentos:
                        resultado["impedimentos"].extend(impedimentos)
                        logger.warning("Pilar '%s' — Impedimento detectado: %s", pilar.get("name"), impedimentos)

                if contexto_obrigatorio:
                    obrigatorios = _encontrar_termos(texto, contexto_obrigatorio)
                    if not obrigatorios:
                        resultado["alertas"].append(
                            f"Conceito '{termo_principal}' encontrado, mas sem contexto obrigatório na proposta."
                        )
            else:
                todos_ausentes.append(termo_principal)

    resultado["termos_encontrados"] = sorted(list(set(todos_encontrados)))
    resultado["termos_ausentes"] = sorted(list(set(todos_ausentes)))
    resultado["impedimentos"] = sorted(list(set(resultado["impedimentos"])))
    resultado["alertas"] = sorted(list(set(resultado["alertas"])))

    if resultado["impedimentos"]:
        resultado["aprovado"] = False
    elif todos_encontrados:
        resultado["aprovado"] = True
    else:
        resultado["aprovado"] = False
        resultado["alertas"].append("Nenhum termo relevante encontrado para este pilar.")

    return resultado

def validar_todos_os_blocos(
    texto: str,
    biblioteca: dict[str, Any],
    max_coordenadores: int = 1,
) -> dict[str, Any]:
    resultados = {}
    
    pillars = biblioteca.get("pillars", [])
    for pilar in pillars:
        pid = pilar.get("id")
        if pid:
            resultados[pid] = validar_pilar(texto, pilar)
            
    return resultados