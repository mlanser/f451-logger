"""Demo for using f451 Labs Logger Module."""

from logging import INFO
from f451_logger.logger import Logger


# =========================================================
#                    D E M O   A P P
# =========================================================
def main():
    # Initialize Logger
    logger = Logger(LOGLVL=INFO)

    print("\n====== [Demo of f451 Labs Logger module] ======")
    print("Showing log message:")
    logger.log("Hello world!", INFO)

    print("\nShowing PrettyPrint:")
    logger.debug("Hello world!")

    print("=============== [End of Demo] =================\n")


if __name__ == '__main__':
    main()
