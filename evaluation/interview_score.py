def interview_score(report):
    """
    Calculate the overall interview score using
    weighted averages from the interview report.
    """

    technical = report.get("technical_score", 0)
    communication = report.get("communication_score", 0)
    confidence = report.get("confidence_score", 0)

    score = (
        technical * 0.6
        + communication * 0.2
        + confidence * 0.2
    )

    return round(score, 2)