"""create a log of everything in the calculator"""
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    filename="log_history",
                    level=logging.DEBUG)

# Creating an object
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Module-level logger. It will track the module hierarchy
logger = logging.getLogger(__name__)

# Application Messages
logger.debug("This is a debug log")
logger.error("Error: Cannot Divide by Zero")
