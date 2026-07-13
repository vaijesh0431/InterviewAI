from interviewer.menu import select_topic
from interviewer.interview_session import InterviewSession

from utils.helpers import print_header
from utils.logger import logger


def main():

    print_header()

    topic = select_topic()

    if topic is None:
        print("Invalid Selection")
        return

    interview = InterviewSession(topic)

    interview.start()


if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print("\n\n❌ Interview Cancelled by User.")

        logger.info("Interview Cancelled by User")

    except Exception as e:

        logger.exception("Unhandled Exception")

        print("\n⚠ An unexpected error occurred.")

        print("Please check logs/interview.log for details.")