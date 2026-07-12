class InterviewMemory:

    def __init__(self):

        self.history = []

    def add(self, question, answer):

        self.history.append({

            "question": question,

            "answer": answer

        })

    def get_context(self):

        context = ""

        for item in self.history:

            context += f"""

Question:
{item['question']}

Answer:
{item['answer']}

"""

        return context