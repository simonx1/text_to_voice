import signal
import sys
from elevenlabs import generate, play

def signal_handler(sig, frame):
    print("\nYou pressed Ctrl+C! Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

print("Enter text to generate and play voice using Eleven Labs. Press Ctrl+C to exit.")

while True:
    try:
        text = input("Enter your text: ")
        audio = generate(
            text=text,
            voice="SzymonK voice",
            model='eleven_multilingual_v1'
        )
        play(audio)
    except KeyboardInterrupt:
        signal_handler(None, None)
