import logging
import time


logger = logging.getLogger("ready-python-logs")
logger.setLevel(logging.DEBUG)

# remove all default handlers
for handler in logger.handlers:
    logger.removeHandler(handler)

# create console handler and set log level to debug
console_handle = logging.StreamHandler()
console_handle.setLevel(logging.DEBUG)

# create formatter with UCT datetime prefix and log-level
formatter = logging.Formatter("%(asctime)sZ %(levelname)s: %(message)s")
logging.Formatter.converter = time.gmtime
console_handle.setFormatter(formatter)

# now the new handler to logger instance
logger.addHandler(console_handle)
