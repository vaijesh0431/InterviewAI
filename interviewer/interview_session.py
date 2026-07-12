from rich.console import Console
from rich.panel import Panel

from speech.recorder import record_audio
from speech.speech_to_text import transcribe
from speech.text_to_speech import speak

from interviewer.question_loader import QuestionLoader

console = Console()


class InterviewSession:

    def __init__(self, topic):
        self.topic = topic
        self.questions = QuestionLoader.load(topic)
        self.answers = []

    def start(self):

        console.print()

        console.print(
            Panel.fit(
                f"🚀 Starting {self.topic.upper()} Interview",
                border_style="magenta",
                title="InterviewAI"
            )
        )

        total_questions = len(self.questions)

        for index, question in enumerate(self.questions, start=1):

            console.print()

            console.print(
                Panel(
                    question["question"],
                    title=f"🎤 Question {index}/{total_questions}",
                    border_style="cyan"
                )
            )

            # AI speaks the question
            speak(question["question"])

            # Record candidate response
            audio = record_audio()

            # Convert speech to text
            answer = transcribe(audio)

            if not answer or answer.strip() == "":
                answer = "No response detected."

            console.print()

            console.print(
                Panel(
                    answer,
                    title="🧑 Candidate Answer",
                    border_style="green"
                )
            )

            self.answers.append(
                {
                    "question": question["question"],
                    "answer": answer
                }
            )

        console.print()

        console.print(
            Panel.fit(
                "✅ Interview Completed Successfully!",
                border_style="green",
                title="InterviewAI"
            )
        )