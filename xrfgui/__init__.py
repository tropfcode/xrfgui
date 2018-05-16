#from . import model, view
import logging
logger = logging.getLogger()
from logging import NullHandler
logger.addHandler(NullHandler())
logging.basicConfig(filename='program.log', level=logging.DEBUG)