from rich.console import Console
from rich.panel import Panel

from speech.recorder import record_audio
from speech.speech_to_text import transcribe
from speech.text_to_speech import speak

from interviewer.question_loader import QuestionLoader

from evaluation.evaluator import evaluate
from evaluation.scoring import overall_score

console = Console()


class InterviewSession:

    def __init__(self, topic):
        self.topic = topic
        self.questions = QuestionLoader.load(topic)

        # Stores raw candidate answers
        self.answers = []

        # Stores complete interview results
        self.results = []

    def start(self):

        console.print()

        console.print(
            Panel.fit(
                f"🚀 Starting {self.topic.upper()} Interview",
                title="InterviewAI",
                border_style="magenta",
            )
        )

        total_questions = len(self.questions)

        for index, question in enumerate(self.questions, start=1):

            # ----------------------------
            # Display Question
            # ----------------------------

            console.print()

            console.print(
                Panel(
                    question["question"],
                    title=f"🎤 Question {index}/{total_questions}",
                    border_style="cyan",
                )
            )

            # AI speaks the question
            speak(question["question"])

            # ----------------------------
            # Record Candidate Response
            # ----------------------------

            audio = record_audio()

            answer = transcribe(audio)

            if not answer or answer.strip() == "":
                answer = "No response detected."

            console.print()

            console.print(
                Panel(
                    answer,
                    title="🧑 Candidate Answer",
                    border_style="green",
                )
            )

            # Store raw answer
            self.answers.append(
                {
                    "question": question["question"],
                    "answer": answer,
                }
            )

            # ----------------------------
            # AI Evaluation
            # ----------------------------

            evaluation = evaluate(
                question["question"],
                answer,
            )

            score = overall_score(evaluation)

            evaluation["overall_score"] = score

            # Store complete result
            self.results.append(
                {
                    "question": question["question"],
                    "answer": answer,
                    "evaluation": evaluation,
                }
            )

            # ----------------------------
            # Display AI Evaluation
            # ----------------------------

            console.print()

            console.print(
                Panel(
                    f"""
📘 Technical Score     : {evaluation.get('technical_score', 0)}/10

💬 Communication Score : {evaluation.get('communication_score', 0)}/10

🎯 Confidence Score    : {evaluation.get('confidence_score', 0)}/10

⭐ Overall Score       : {score}/10

✅ Accuracy            : {evaluation.get('accuracy', 'Unknown')}
""",
                    title="📊 AI Evaluation",
                    border_style="green",
                )
            )

            # ----------------------------
            # Display Strengths
            # ----------------------------

            strengths = evaluation.get("strengths", [])

            if strengths:

                console.print(
                    Panel(
                        "\n".join(f"✔ {item}" for item in strengths),
                        title="💪 Strengths",
                        border_style="blue",
                    )
                )

            # ----------------------------
            # Display Weaknesses
            # ----------------------------

            weaknesses = evaluation.get("weaknesses", [])

            if weaknesses:

                console.print(
                    Panel(
                        "\n".join(f"• {item}" for item in weaknesses),
                        title="⚠ Weaknesses",
                        border_style="red",
                    )
                )

            # ----------------------------
            # Missing Concepts
            # ----------------------------

            missing = evaluation.get("missing_concepts", [])

            if missing:

                console.print(
                    Panel(
                        "\n".join(f"• {item}" for item in missing),
                        title="📚 Missing Concepts",
                        border_style="yellow",
                    )
                )

            # ----------------------------
            # AI Feedback
            # ----------------------------

            console.print(
                Panel(
                    evaluation.get(
                        "feedback",
                        "No feedback available.",
                    ),
                    title="💡 AI Feedback",
                    border_style="magenta",
                )
            )

        # ----------------------------
        # Interview Completed
        # ----------------------------

        console.print()

        console.print(
            Panel.fit(
                "🎉 Interview Completed Successfully!",
                title="InterviewAI",
                border_style="green",
            )
        )