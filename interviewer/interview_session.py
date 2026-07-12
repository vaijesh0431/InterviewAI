from email.mime import audio
from multiprocessing import context

from rich.console import Console
from rich.panel import Panel

from interviewer import followup
from speech.recorder import record_audio
from speech.speech_to_text import transcribe
from speech.text_to_speech import speak

from interviewer.question_loader import QuestionLoader
from interviewer.memory import InterviewMemory
from interviewer.followup import generate_followup

from evaluation.evaluator import evaluate
from evaluation.scoring import overall_score

from config import MAX_FOLLOWUPS

console = Console()


class InterviewSession:

    def __init__(self, topic):
        self.topic = topic
        self.questions = QuestionLoader.load(topic)

        # Stores raw candidate answers
        self.answers = []

        # Stores complete interview results
        self.results = []

        # Interview memory
        self.memory = InterviewMemory()

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

            # ---------------------------------
            # Display Question
            # ---------------------------------

            console.print()

            console.print(
                Panel(
                    question["question"],
                    title=f"🎤 Question {index}/{total_questions}",
                    border_style="cyan",
                )
            )

            speak(question["question"])

            # ---------------------------------
            # Candidate Answer
            # ---------------------------------

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

            self.answers.append(
                {
                    "question": question["question"],
                    "answer": answer,
                }
            )

            # Store in interview memory
            self.memory.add(
                question["question"],
                answer,
            )

            # ---------------------------------
            # Evaluate Main Answer
            # ---------------------------------

            evaluation = evaluate(
                question["question"],
                answer,
            )

            score = overall_score(evaluation)

            evaluation["overall_score"] = score

            console.print()

            console.print(
                Panel(
                    f"""
📘 Technical Score     : {evaluation.get('technical_score',0)}/10

💬 Communication Score : {evaluation.get('communication_score',0)}/10

🎯 Confidence Score    : {evaluation.get('confidence_score',0)}/10

⭐ Overall Score       : {score}/10

✅ Accuracy            : {evaluation.get('accuracy','Unknown')}
""",
                    title="📊 AI Evaluation",
                    border_style="green",
                )
            )

            strengths = evaluation.get("strengths", [])

            if strengths:
                console.print(
                    Panel(
                        "\n".join(f"✔ {item}" for item in strengths),
                        title="💪 Strengths",
                        border_style="blue",
                    )
                )

            weaknesses = evaluation.get("weaknesses", [])

            if weaknesses:
                console.print(
                    Panel(
                        "\n".join(f"• {item}" for item in weaknesses),
                        title="⚠ Weaknesses",
                        border_style="red",
                    )
                )

            missing = evaluation.get("missing_concepts", [])

            if missing:
                console.print(
                    Panel(
                        "\n".join(f"• {item}" for item in missing),
                        title="📚 Missing Concepts",
                        border_style="yellow",
                    )
                )

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



            # ---------------------------------
            # Adaptive Follow-up Questions
            # ---------------------------------

            current_question = question["question"]
            current_answer = answer
            current_evaluation = evaluation

            for i in range(MAX_FOLLOWUPS):

                context = self.memory.get_context()

                followup = generate_followup(
                    current_question,
                    current_answer,
                    current_evaluation,
                    context,
                )

                console.print()

                console.print(
                    Panel(
                        followup,
                        title=f"🔄 Follow-up Question {i + 1}/{MAX_FOLLOWUPS}",
                        border_style="blue",
                    )
                )

                speak(followup)

                audio = record_audio()

                followup_answer = transcribe(audio)

                if not followup_answer or followup_answer.strip() == "":
                    followup_answer = "No response detected."

                console.print()

                console.print(
                    Panel(
                        followup_answer,
                        title=f"🧑 Follow-up Answer {i + 1}",
                        border_style="green",
                    )
                )

                followup_result = evaluate(
                    followup,
                    followup_answer,
                )

                followup_score = overall_score(followup_result)

                followup_result["overall_score"] = followup_score

                console.print()

                console.print(
                    Panel(
                        f"""
                        📘 Technical Score     : {followup_result.get('technical_score',0)}/10

                        💬 Communication Score : {followup_result.get('communication_score',0)}/10

                        🎯 Confidence Score    : {followup_result.get('confidence_score',0)}/10

                        ⭐ Overall Score       : {followup_score}/10

                        ✅ Accuracy            : {followup_result.get('accuracy','Unknown')}
                    """,
                        title=f"📊 Follow-up Evaluation {i + 1}",
                        border_style="green",
                    )
                )

                console.print(
                    Panel(
                        followup_result.get(
                            "feedback",
                            "No feedback available.",
                        ),
                        title="💡 Follow-up Feedback",
                        border_style="magenta",
                    )
                )

                # Store follow-up in interview memory
                self.memory.add(
                    followup,
                    followup_answer
                )

                # Store interview result
                self.results.append(
                    {
                        "question": current_question,
                        "answer": current_answer,
                        "evaluation": current_evaluation,
                        "main_score": current_evaluation.get("overall_score", score),

                        "followup": followup,
                        "followup_answer": followup_answer,
                        "followup_score": followup_score,
                        "followup_evaluation": followup_result,
                    }
                )

                # Update context for the next follow-up
                current_question = followup
                current_answer = followup_answer
                current_evaluation = followup_result

        # ---------------------------------
        # Interview Completed
        # ---------------------------------

        console.print()

        console.print(
            Panel.fit(
                "🎉 Interview Completed Successfully!",
                title="InterviewAI",
                border_style="green",
            )
        )