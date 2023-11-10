# f451 Labs Logger module v0.2.0

## Overview

The *f451 Labs Logger* module encapsulates the default Python `Logging` class and adds a few more features that are commonly used in *f451 Labs* projects.

## Install

This module is not (yet) available on PyPi. however, you can still use `pip` to install the module directly from Github (see below).

### Dependencies

This module is dependent on the following libraries:

- [logging](https://docs.python.org/3/howto/logging.html)
- [pprint](https://docs.python.org/3/library/pprint.html)

### Installing from Github using `pip`

You can use `pip install` to install this module directly from Github as follows:

Using HTTPS:

```bash
$ pip install 'f451-logger @ git+https://github.com/mlanser/f451-logger.git'
```

Using SSH:

```bash
$ pip install 'f451-logger @ git+ssh://git@github.com:mlanser/f451-logger.git'
```

## How to use

Using the module is straightforward. Simply `import` it to you code and instantiate a logger object which you can then use throught your code.

```Python
from f451_logger.logger import Logger

# Instantiate using defaults ...
logger = Logger()

# ... or with custom log level and log file values
logger = Logger(logLvl=logging.ERROR, logFile="path/to/mylogfile.log")

# Call 'log_xxxx' methods to log messages
logger.log_info("Hello world!")
logger.log_error("Oops! Something broke :-(")

# Call 'debug' method to show message in console
logger.debug("Hello world!")

myVar = 2
logger.debug(myVar)
```
