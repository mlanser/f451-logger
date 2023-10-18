"""f451 Labs Logger module.

The f451 Labs Logger module encapsulates the default Python 'Logging' class
and adds a few more features that are commonly used in f451 Labs projects.

Dependencies:
 - logging
 - pprint
 - tomllib / tomli
"""

import logging
import pprint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


# =========================================================
#          G L O B A L S   A N D   H E L P E R S
# =========================================================
class Logger:
    def __init__(self, name="f451-Log", logLvl=logging.NOTSET, logFile=None):
        """Initialize logger

        Args:
            logLvl:
                Default log level
            logFile:
                Path object for log file
        """
        self._LOG = self._init_logger(name, logLvl, logFile)
        self._PP = pprint.PrettyPrinter(indent=4)

    def _init_logger(self, name, logLvl, logFile):
        """Initialize Logger

        We always initialize the logger with a stream 
        handler. But file handler is only created if 
        a file name has been provided in settings.
        """
        logger = logging.getLogger(name)
        logger.setLevel(logLvl)

        if logFile:
            fileHandler = logging.FileHandler(logFile)
            fileHandler.setLevel(logLvl)
            fileHandler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s: %(message)s"))
            logger.addHandler(fileHandler)

        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logLvl)
        streamHandler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s: %(message)s"))
        logger.addHandler(streamHandler)

        return logger

    def log(self, lvl, msg):
        """Wrapper of Logger.log()"""
        self._LOG.log(lvl, msg)

    def log_error(self, msg):
        """Wrapper of Logger.error()"""
        self._LOG.error(msg)

    def log_info(self, msg):
        """Wrapper of Logger.info()"""
        self._LOG.info(msg)

    def log_debug(self, msg):
        """Wrapper of Logger.debug()"""
        self._LOG.debug(msg)

    def pprint(self, val):
        self._PP.pprint(val)
