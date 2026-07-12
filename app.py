from interviewer.menu import select_topic
from interviewer.interview_session import InterviewSession

from utils.helpers import print_header


def main():

    print_header()

    topic = select_topic()

    if topic is None:
        print("Invalid Selection")
        return

    interview = InterviewSession(topic)

    interview.start()


if __name__ == "__main__":
    main()