"""Demo for using f451 Labs Uploader Module."""

from logging import INFO
from f451_logger.logger import Logger

# =========================================================
#                    D E M O   A P P
# =========================================================
def main():
    """Write 'Hello world!' to log system."""

    logger = Logger(logLvl=INFO)

    print("=== f451 Labs Logger module ===")
    print("Showing log message:")
    logger.log(INFO, "Hello world!")


    print("\nShowing PrettyPrint:")
    logger.debug("Hello world!")


if __name__ == "__main__":
    main()