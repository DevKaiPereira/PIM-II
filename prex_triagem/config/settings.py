import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    # Rodando como executável compilado (PyInstaller)
    ROOT_DIR = Path(sys._MEIPASS)
    BASE_EXEC_DIR = Path(sys.executable).parent
else:
    # Rodando como script normal (.py)
    ROOT_DIR = Path(__file__).resolve().parent.parent
    BASE_EXEC_DIR = ROOT_DIR

PASTA_PDFS = BASE_EXEC_DIR / "data" / "pdfs_entrada"
PASTA_EDITAIS_JSON = BASE_EXEC_DIR / "data" / "editais_json"
PASTA_RELATORIOS = BASE_EXEC_DIR / "relatorios"
PASTA_LOGS = BASE_EXEC_DIR / "logs"
ARQUIVO_BIBLIOTECA = ROOT_DIR / "biblioteca_termos.json"
RELATORIO_CONSOLIDADO = PASTA_RELATORIOS / "consolidado.csv"
ARQUIVO_LOG = PASTA_LOGS / "triagem.log"
MAX_COORDENADORES = 1
LIMIAR_ALTO_MERITO = 25
LIMIAR_MEDIO_MERITO = 12
EXTENSOES_ACEITAS = [".pdf"]
TAMANHO_MINIMO_TEXTO = 100
ENCODING_SAIDA = "utf-8"
VERBOSE = True
LARGURA_SEPARADOR = 70