from config import APP_NAME, VERSION
from utils.helpers import print_header, success, info
from utils.logger import logger


def main():
    print_header()

    info(f"Application : {APP_NAME}")
    info(f"Version     : {VERSION}")

    logger.info("Application Started")

    success("Environment Initialized Successfully")

    print()
    print("Welcome to InterviewAI")
    print("Your AI Voice Interview Coach")


if __name__ == "__main__":
    main()