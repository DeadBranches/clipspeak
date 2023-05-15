import argparse
from clipspeak import clipboard, speech

def main():

    # Create an argument parser object
    parser = argparse.ArgumentParser(description="Synthesize and speak text from clipboard.")
    # Add an argument for the speech configuration set
    parser.add_argument("-c", "--config_set", default="aria", help="The speech configuration set to use.")
    # Parse the arguments
    args = parser.parse_args()
    # Get the clipboard contents
    text = clipboard.get_clipboard()
    # Create a text to speech object with the given configuration set
    tts = speech.TextToSpeech(config_set=args.config_set)
    # Synthesize and speak the text
    audio_data = tts.synthesize_text(text)


if __name__ == "__main__":
    main()