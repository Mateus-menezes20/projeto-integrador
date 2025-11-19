import logging
from logging.handlers import RotatingFileHandler
import os

# Criar pasta de logs caso não exista
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Caminho do arquivo de log
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Configuração do logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Handler com rotação (5 arquivos de até 1MB cada)
handler = RotatingFileHandler(
    LOG_FILE, 
    maxBytes=1_000_000, 
    backupCount=5,
    encoding="utf-8"
)

# Formato do log
formatter = logging.Formatter(
    "%(asctime)s - USER:%(user)s - ACTION:%(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

# Função auxiliar para registrar logs com usuário
def log(user, action):
    extra = {"user": user}
    logger.info(action, extra=extra)
