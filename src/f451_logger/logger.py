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
import json


# =========================================================
#              M I S C .   C O N S T A N T S
# =========================================================
DEF_LOG_NAME = "f451-Log"   # Default logger name


# =========================================================
#    K E Y W O R D S   F O R   C O N F I G   F I L E S
# =========================================================
KWD_LOG_NAME = "LOGNAME"
KWD_LOG_LEVEL = "LOGLVL"
KWD_LOG_FILE = "LOGFILE"


# =========================================================
#                     M A I N   C L A S S
# =========================================================
class Logger:
    """f451 Labs core Logger class.

    This class standardizes and simplifies logging across f451 Labs projects
    by wrapping the default Python 'logging' module/class. It also includes 
    the 'pprint' for displaying debug messages.

    NOTE: attributes follow same naming convention as used 
    in the 'settings.toml' file. This makes it possible to pass 
    in the 'config' object (or any other dict) as is.

    NOTE: we let users provide an entire 'dict' object with settings as 
    key-value pairs, or as individual settings. User can combine both and,
    for example, provide a standard 'config' object as well as individual
    settings which could override the values in the 'config' object.

    Example:
        myLogger = Logger()                 # Only use default values
        myLogger = Logger(config)           # Use values from 'config' 
        myLogger = Logger(key=val)          # Use val
        myLogger = Logger(config, key=val)  # Use values from 'config' and also use 'val' 

    Attributes:
        LOGNAME:    Logger name as 'str'
        LOGLVL:     Log level as 'int'
        LOGFILE:    Log file as 'str' or 'Path' object
    """
    def __init__(self, *args, **kwargs):
        """Initialize logger

        Args:
            args:
                User can provide single 'dict' with settings
            kwargs:
                User can provide individual settings as key-value pairs
        """
        self._PP = pprint.PrettyPrinter(indent=4)

        # We combine 'args' and 'kwargs' to allow users to provide the entire 
        # 'config' object and/or individual settings (which could override 
        # values in 'config').
        settings = {**args[0], **kwargs} if args and type(args[0]) is dict else kwargs
        self._LOG = self._init_logger(**settings)

    def _init_logger(self, **kwargs):
        """Initialize Logger

        We always initialize the logger with a stream 
        handler. But file handler is only created if 
        a file name has been provided in settings.

        Args:
            kwargs:
                Core settings as key-value pairs in 'dict'

        Returns:
            Initialized 'logger' object
        """
        logName = kwargs.get(KWD_LOG_NAME, DEF_LOG_NAME) 
        logLvl = kwargs.get(KWD_LOG_LEVEL, logging.NOTSET)
        logFile = kwargs.get(KWD_LOG_FILE)

        logger = logging.getLogger(logName)
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

    def debug(self, val, strict=True):
        """Wrapper of pprint.pprint()
        
        Args:
            val: Value to be 'pretty' printed
            strict: If 'True', then values are printed as-is
        """
        if isinstance(val, dict) and not strict:
            self._PP.pprint(json.dumps(val, indent=4))
        else:    
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
