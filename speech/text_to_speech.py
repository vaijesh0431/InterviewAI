import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Speech properties
engine.setProperty("rate", 170)      # Speed of speech
engine.setProperty("volume", 1.0)    # Volume (0.0 to 1.0)


def speak(text):
    """
    Convert text to speech.
    """

    print()
    print(f"🤖 AI: {text}")

    engine.say(text)
    engine.runAndWait()