def recommendation(score):
    """
    Generate the hiring recommendation based on
    the overall interview score.
    """

    if score >= 9:
        return {
            "status": "Strong Hire",
            "message": "Excellent technical knowledge and communication. Highly recommended for the role."
        }

    elif score >= 8:
        return {
            "status": "Hire",
            "message": "Good performance with solid technical understanding. Recommended for hiring."
        }

    elif score >= 6:
        return {
            "status": "Borderline",
            "message": "Candidate shows potential but requires improvement in some areas."
        }

    return {
        "status": "Needs Improvement",
        "message": "Candidate should strengthen technical concepts before being considered for the role."
    }