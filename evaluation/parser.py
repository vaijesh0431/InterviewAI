import json


DEFAULT_RESPONSE = {
    "technical_score": 0,
    "communication_score": 0,
    "confidence_score": 0,
    "accuracy": "Unknown",
    "strengths": [],
    "weaknesses": [],
    "missing_concepts": [],
    "feedback": "Unable to evaluate answer."
}


def extract_json(response):

    try:

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            return DEFAULT_RESPONSE

        cleaned = response[start:end + 1]

        return json.loads(cleaned)

    except Exception:

        return DEFAULT_RESPONSE