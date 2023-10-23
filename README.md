# f451 Labs Logger module

## Overview

The *f451 Labs Logger* module encapsulates the default Python `Logging` class and adds a few more features that are commonly used in *f451 Labs* projects.

## Install

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Convallis a cras semper auctor neque vitae.

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

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Convallis a cras semper auctor neque vitae.

```Python
# Using defaults ...
logger = Logger()

# ... or with custom log level and log file values
logger = Logger(logLvl=logging.ERROR, logFile="path/to/mylogfile.log")
```
