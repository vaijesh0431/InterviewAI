class Statistics:
    """
    Utility class for statistical calculations.
    """

    @staticmethod
    def average(scores):
        """
        Calculate the average of a list of scores.
        """

        if not scores:
            return 0

        return round(sum(scores) / len(scores), 2)

    @staticmethod
    def highest(scores):
        """
        Return the highest score.
        """

        return max(scores) if scores else 0

    @staticmethod
    def lowest(scores):
        """
        Return the lowest score.
        """

        return min(scores) if scores else 0