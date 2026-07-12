import json

from ollama import chat

from evaluation.prompts import SYSTEM_PROMPT

from evaluation.parser import extract_json


MODEL = "llama3.1:8b"


def evaluate(question, answer):

    prompt = f"""
Interview Question:

{question}

Candidate Answer:

{answer}

Evaluate the answer objectively.

Return ONLY valid JSON.

Do not include markdown.

Do not include explanations.

Do not include ```json.

Return only the JSON object.
"""

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    text = response["message"]["content"]

    try:
        return extract_json(text)

    except json.JSONDecodeError:

        return {
        "technical_score": 0,
        "communication_score": 0,
        "confidence_score": 0,
        "accuracy": "Unknown",
        "strengths": [],
        "weaknesses": [],
        "missing_concepts": [],
        "feedback": "Failed to parse AI response."
    }