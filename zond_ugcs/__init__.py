import logging

# Set up logger
log = logging.getLogger("libzond")
log.setLevel("INFO")
log.propagate = 0
ch = logging.StreamHandler()
FORMAT = "[%(asctime)s] - %(name)s - %(levelname)s: %(message)s"
formatter = logging.Formatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)
log.addHandler(ch)

from zond_ugcs.read import read
