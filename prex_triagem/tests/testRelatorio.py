import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from prex_triagem.src.relatorio import determinar_status


class TestRelatorioStatus(unittest.TestCase):
    def test_status_apto_quando_todos_blocos_aprovados_sem_impedimentos(self):
        resultados_blocos = {
            "bloco_1": {"aprovado": True, "impedimentos": []},
            "bloco_2": {"aprovado": True, "impedimentos": []},
            "bloco_3": {"aprovado": True, "impedimentos": []},
            "bloco_4": {"aprovado": True, "impedimentos": []},
        }
        resultado_merito = {"pontuacao_total": 0}
        self.assertEqual(determinar_status(resultados_blocos, resultado_merito), "APTO")

    def test_status_inapto_quando_ha_impedimento_em_algum_bloco(self):
        resultados_blocos = {
            "bloco_1": {"aprovado": True, "impedimentos": []},
            "bloco_2": {"aprovado": True, "impedimentos": ["impedimento"]},
            "bloco_3": {"aprovado": True, "impedimentos": []},
            "bloco_4": {"aprovado": True, "impedimentos": []},
        }
        resultado_merito = {"pontuacao_total": 42}
        self.assertEqual(determinar_status(resultados_blocos, resultado_merito), "INAPTO")

    def test_status_alerta_quando_ha_bloco_nao_aprovado_sem_impedimentos(self):
        resultados_blocos = {
            "bloco_1": {"aprovado": True, "impedimentos": []},
            "bloco_2": {"aprovado": False, "impedimentos": []},
            "bloco_3": {"aprovado": True, "impedimentos": []},
            "bloco_4": {"aprovado": True, "impedimentos": []},
        }
        resultado_merito = {"pontuacao_total": 42}
        self.assertEqual(determinar_status(resultados_blocos, resultado_merito), "ALERTA")


if __name__ == "__main__":
    unittest.main(verbosity=2)
