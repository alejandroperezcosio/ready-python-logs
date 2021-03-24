import logging
import time


log = logging.getLogger("ready-python-logs")
log.setLevel(logging.DEBUG)

# remove all default handlers
for handler in log.handlers:
    log.removeHandler(handler)

# create console handler and set log level to debug
console_handle = logging.StreamHandler()
console_handle.setLevel(logging.DEBUG)

# create formatter with UCT datetime prefix and log-level
formatter = logging.Formatter("%(asctime)sZ %(levelname)s: %(message)s")
logging.Formatter.converter = time.gmtime
console_handle.setFormatter(formatter)

# now the new handler to logger instance
log.addHandler(console_handle)
