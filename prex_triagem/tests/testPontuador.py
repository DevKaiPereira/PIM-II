import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from prex_triagem.src.pontuador import calcular_pontuacao_merito


class TestPontuadorMerito(unittest.TestCase):
    def test_pontua_com_hifen_e_acentos(self):
        config_bloco5 = {
            "termos_de_merito": {
                "impacto_social": {
                    "termos": ["impacto social"],
                    "pontos_por_ocorrencia": 2,
                    "max_pontos": 10,
                },
                "indissociabilidade": {
                    "termos": ["tríade", "ensino pesquisa extensao"],
                    "pontos_por_ocorrencia": 3,
                    "max_pontos": 9,
                },
                "metodologia": {
                    "termos": ["metodologia", "plano de trabalho"],
                    "pontos_por_ocorrencia": 1,
                    "max_pontos": 7,
                },
            },
            "limiares": {"alto_merito": 25, "medio_merito": 12},
        }

        texto = (
            "A proposta descreve impacto-social relevante. "
            "Ha uma tríade ensino-pesquisa-extensao bem definida. "
            "A metodologia inclui um plano de trabalho e cronograma. "
            "Metodologia aplicada com indicadores."
        )

        resultado = calcular_pontuacao_merito(texto, config_bloco5)
        self.assertGreater(resultado["pontuacao_total"], 0)

        detalhes = resultado["detalhes_categorias"]
        termos_impacto = [t["termo"] for t in detalhes["impacto_social"]["termos_encontrados"]]
        self.assertIn("impacto social", termos_impacto)

        termos_ind = [t["termo"] for t in detalhes["indissociabilidade"]["termos_encontrados"]]
        self.assertIn("tríade", termos_ind)


if __name__ == "__main__":
    unittest.main(verbosity=2)
