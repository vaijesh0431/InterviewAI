from analytics.statistics import Statistics


class Analytics:
    """
    Performs analytics on interview history.
    """

    # Database Column Indexes
    OVERALL_SCORE = 5

    def __init__(self, rows):
        self.rows = rows

    def scores(self):
        """
        Extract all overall interview scores.
        """

        return [
            row[self.OVERALL_SCORE]
            for row in self.rows
        ]

    def best_score(self):
        """
        Highest interview score.
        """

        return Statistics.highest(
            self.scores()
        )

    def average_score(self):
        """
        Average interview score.
        """

        return Statistics.average(
            self.scores()
        )

    def total_interviews(self):
        """
        Number of interviews completed.
        """

        return len(self.rows)