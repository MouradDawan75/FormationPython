import logging
from logging.handlers import RotatingFileHandler

# RotatingFileHandler donne la possibilté de faire piviter les fichiers de logs en fonction de leur taille

logger = logging.getLogger('Rotation_logger')
logger.setLevel(logging.INFO)

# si maxBytes = 0: la rotation ne se produira jamais
handler = RotatingFileHandler('28_Logs/rotating.log', maxBytes=20, mode='a', encoding='utf-8', backupCount=5)
logger.addHandler(handler)


for i in range(1,10):
    logger.info(f'Ligne numéro: {i}')