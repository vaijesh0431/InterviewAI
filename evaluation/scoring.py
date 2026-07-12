def overall_score(result):

    technical = result.get("technical_score", 0)
    communication = result.get("communication_score", 0)
    confidence = result.get("confidence_score", 0)

    return round(
        (technical * 0.6)
        + (communication * 0.2)
        + (confidence * 0.2),
        2,
    )