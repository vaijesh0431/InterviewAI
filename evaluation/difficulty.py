def difficulty(score):
    """
    Determine follow-up question difficulty based on
    the candidate's technical score.
    """

    if score >= 8:
        return "hard"

    elif score >= 5:
        return "medium"

    return "easy"