from ollama import chat


MODEL = "llama3.1:8b"


def ask_llama(prompt):

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]