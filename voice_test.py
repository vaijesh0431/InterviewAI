from speech.recorder import record_audio
from speech.speech_to_text import transcribe
from llm.ollama_client import ask_llama
from speech.text_to_speech import speak
from utils.logger import logger


def main():
    try:
        print("=" * 50)
        print("        InterviewAI Voice Test")
        print("=" * 50)

        # Record audio
        audio = record_audio()

        # Convert speech to text
        text = transcribe(audio)

        # Check if speech was detected
        if not text or text.strip() == "":
            print("❌ No speech detected. Please try again.")
            logger.warning("No speech detected during recording.")
            return

        print(f"\nYou: {text}")

        # Get AI response
        response = ask_llama(text)

        print(f"\nAI: {response}")

        # Speak the response
        speak(response)

        logger.info("Voice test completed successfully.")

    except Exception as e:
        logger.exception("Error occurred during voice test.")
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()