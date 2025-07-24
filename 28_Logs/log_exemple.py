import logging

# level: debug, info, warning, error, critical

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y - %H:%M",
    filename="28_Logs/app.log",
    filemode='a',
    encoding='utf-8'
)

logging.debug('debug.....')
logging.info('info....')
logging.warning('warning.....')
logging.error('error....')
logging.critical('critical..........')

# En plus du root logger, on a la possibilité d'ajouter d'autres loggers
# Par défaut les autres héritent de la conf. du root logger (basicConfig)

my_logger = logging.getLogger('logger_console')

my_logger.setLevel(logging.DEBUG)
my_logger.addHandler(logging.StreamHandler())

my_logger.debug('debug message................')
