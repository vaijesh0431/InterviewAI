from ollama import chat

from evaluation.difficulty import difficulty
from interviewer.persona import INTERVIEWER_PERSONA

MODEL = "llama3.1:8b"


def generate_followup(question, answer, evaluation, context):
    """
    Generate an intelligent follow-up question based on the
    candidate's previous answer and evaluation.
    """

    # Determine follow-up difficulty from technical score
    difficulty_level = difficulty(evaluation["technical_score"])

    prompt = f"""
{INTERVIEWER_PERSONA}

Interview Context:
{context}

Current Question:
{question}

Candidate Answer:
{answer}

Evaluation Summary:
Technical Score: {evaluation['technical_score']}/10
Communication Score: {evaluation['communication_score']}/10
Confidence Score: {evaluation['confidence_score']}/10

Strengths:
{', '.join(evaluation['strengths']) if evaluation['strengths'] else 'None'}

Weaknesses:
{', '.join(evaluation['weaknesses']) if evaluation['weaknesses'] else 'None'}

Missing Concepts:
{', '.join(evaluation['missing_concepts']) if evaluation['missing_concepts'] else 'None'}

Generate ONE {difficulty_level}-level technical follow-up question.

Rules:
1. Ask exactly ONE question.
2. Do NOT repeat previous questions.
3. Focus on the candidate's weak areas or missing concepts.
4. The question should naturally continue the conversation.
5. Keep it under 25 words.
6. Do NOT provide explanations, hints, or answers.
7. Return ONLY the question.
"""

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": INTERVIEWER_PERSONA
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()