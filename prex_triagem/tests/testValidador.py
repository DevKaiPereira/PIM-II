import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from prex_triagem.src.validador import validar_pilar, validar_todos_os_pilares

CONFIG_PILAR_1 = {
    "id": "P1",
    "name": "Pilar 1 - Admissibilidade",
    "processes": [
        {
            "name": "Exercício Pleno",
            "concepts": [
                {
                    "termo_principal": "em exercicio",
                    "sinonimos": ["servidor ativo", "docente efetivo", "ifb"],
                    "contexto_obrigatorio": [],
                    "contexto_negacao": ["afastado para pos-graduacao", "licenca premio"]
                }
            ]
        }
    ]
}

class TestValidadorPilares(unittest.TestCase):

    def test_pilar_aprovado_com_termo_positivo(self):
        texto = "o proponente esta em exercicio pleno no campus ifb"
        resultado = validar_pilar(texto, CONFIG_PILAR_1)
        self.assertTrue(resultado["aprovado"])
        self.assertIn("em exercicio", resultado["termos_encontrados"])
        self.assertEqual(resultado["impedimentos"], [])

    def test_pilar_inapto_com_impedimento_afastamento(self):
        texto = "servidor ifb em exercicio, mas afastado para pos-graduacao desde 2023"
        resultado = validar_pilar(texto, CONFIG_PILAR_1)
        self.assertFalse(resultado["aprovado"])
        self.assertIn("afastado para pos-graduacao", resultado["impedimentos"])

    def test_pilar_reprovado_sem_termos(self):
        texto = "este documento descreve a proposta de trabalho da equipe"
        resultado = validar_pilar(texto, CONFIG_PILAR_1)
        self.assertFalse(resultado["aprovado"])
        self.assertEqual(resultado["impedimentos"], [])
        self.assertTrue(len(resultado["alertas"]) > 0)

    def test_validar_todos_os_pilares(self):
        biblioteca = {"pillars": [CONFIG_PILAR_1]}
        texto = "servidor docente efetivo no instituto federal"
        resultados = validar_todos_os_pilares(texto, biblioteca)
        self.assertIn("P1", resultados)
        self.assertTrue(resultados["P1"]["aprovado"])

if __name__ == "__main__":
    unittest.main(verbosity=2)