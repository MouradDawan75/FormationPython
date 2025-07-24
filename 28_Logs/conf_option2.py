import logging

error_logger = logging.getLogger('error_logger')
info_logger = logging.getLogger('info_logger')

info_logger.setLevel(logging.INFO)
error_logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s: %(message)s')

error_handler = logging.FileHandler('28_Logs/erros.log', mode='a', encoding='utf-8')
info_handler = logging.FileHandler('28_Logs/infos.log', mode='a', encoding='utf-8')

console_handler = logging.StreamHandler()

error_handler.setFormatter(formatter)
info_handler.setFormatter(formatter)

error_handler.setLevel(logging.ERROR) # cette écrase la conf initiale

error_logger.addHandler(error_handler)
info_logger.addHandler(info_handler)

info_logger.info('info..............')
error_logger.info('info..........')
error_logger.error('error..........')