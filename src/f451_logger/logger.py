"""f451 Labs Logger module.

The f451 Labs Logger module encapsulates the default Python 'Logging' class
and adds a few more features that are commonly used in f451 Labs projects.

Dependencies:
 - logging
 - pprint

How to use:
    logger = Logger()
    logger = Logger(logLvl=logging.ERROR, logFile="path/to/mylogfile.log")
"""

import logging
import pprint


# =========================================================
#                     M A I N   C L A S S
# =========================================================
class Logger:
    """f451 Labs core Logger class.

    This class standardizes and simplifies logging across f451 Labs projects
    by wrapping the default Python 'logging' module/class. It also includes 
    the 'pprint' for displaying debug messages.

    Attributes:
        name: Name of 'logger' as 'str'
        logLvl: Default log level as 'int'
        logFile: Default log file as 'str' or 'Path' object
    """
    def __init__(self, name="f451-Log", logLvl=logging.NOTSET, logFile=None):
        """Initialize logger

        Args:
            logLvl: Default log level as 'int'
            logFile: Path object for log file
        """
        self._LOG = self._init_logger(name, logLvl, logFile)
        self._PP = pprint.PrettyPrinter(indent=4)

    def _init_logger(self, name, logLvl, logFile):
        """Initialize Logger

        We always initialize the logger with a stream 
        handler. But file handler is only created if 
        a file name has been provided in settings.

        Args:
            name: Name of logger as 'str'
            logLvl: Default log level as 'int'
            logFile: Path object for log file

        Returns:
            Initialized 'logger' object
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

    def debug(self, val):
        """Wrapper of pprint.pprint()
        
        Args:
            val: Value to be 'pretty' printed.
        """
        self._PP.pprint(val)

    def log(self, msg, lvl=logging.DEBUG):
        """Wrapper of Logger.log()
        
        Args:
            msg: Log message as 'str'
            lvl: Logging level as 'int'. Default is 'logging.DEBUG'
        """
        self._LOG.log(lvl, msg)

    def log_debug(self, msg):
        """Wrapper of Logger.debug()
        
        Args:
            msg: Log message as 'str'
        """
        self._LOG.debug(msg)

    def log_info(self, msg):
        """Wrapper of Logger.info()
        
        Args:
            msg: Log message as 'str'
        """
        self._LOG.info(msg)

    def log_warning(self, msg):
        """Wrapper of Logger.warning()
        
        Args:
            msg: Log message as 'str'
        """
        self._LOG.warning(msg)

    def log_error(self, msg):
        """Wrapper of Logger.error()
        
        Args:
            msg: Log message as 'str'
        """
        self._LOG.error(msg)
