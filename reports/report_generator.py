from statistics import mean


class ReportGenerator:

    def __init__(self, results):
        self.results = results

    def generate(self):

        technical = []
        communication = []
        confidence = []

        strengths = []
        weaknesses = []
        missing = []

        overall_scores = []

        for item in self.results:

            evaluation = item["evaluation"]

            technical.append(
                evaluation.get("technical_score", 0)
            )

            communication.append(
                evaluation.get("communication_score", 0)
            )

            confidence.append(
                evaluation.get("confidence_score", 0)
            )

            overall_scores.append(
                item.get("main_score", 0)
            )

            strengths.extend(
                evaluation.get("strengths", [])
            )

            weaknesses.extend(
                evaluation.get("weaknesses", [])
            )

            missing.extend(
                evaluation.get("missing_concepts", [])
            )

        report = {

            "technical_score": round(mean(technical), 2),

            "communication_score": round(mean(communication), 2),

            "confidence_score": round(mean(confidence), 2),

            "overall_score": round(mean(overall_scores), 2),

            "strengths": sorted(set(strengths)),

            "weaknesses": sorted(set(weaknesses)),

            "missing_concepts": sorted(set(missing)),
        }

        return report