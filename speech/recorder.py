import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path

SAMPLE_RATE = 16000

OUTPUT_DIR = Path("audio/recordings")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def record_audio(duration=8):

    print("\nRecording...")

    recording = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
    )

    sd.wait()

    filepath = OUTPUT_DIR / "recording.wav"

    write(filepath, SAMPLE_RATE, recording)

    print("Recording Complete.")

    return filepath