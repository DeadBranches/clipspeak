# A dictionary of speech_config options
import azure.cognitiveservices.speech as speechsdk
import configparser
import os

SPEECH_CONFIG_OPTIONS = {
    "aria": {
        "voice_name": "en-US-AriaNeural",
        "voice_pitch": "0",
        "voice_rate": "0",
        "voice_volume": "100",
        "voice_style": None
    },
    "grace": {
        "voice_name": "en-US-GraceNeural",
        "voice_pitch": "0",
        "voice_rate": "0",
        "voice_volume": "100",
        "voice_style": None
    }
}

# Get the home directory of the current user
home_dir = os.path.expanduser("~")
# Join it with the relative path of the config file
CONFIG_FILE_PATH = os.path.join(home_dir, ".config", "config.ini")

class TextToSpeech:
    """A class that performs text to speech using Azure Cognitive Services."""
    def __init__(self, config_set="aria"):
        """Initialize the speech config and synthesizer objects."""
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_PATH)
        azure_key = config.get(config_set, "key", fallback=config.get("Azure", "key", fallback=""))
        service_region = config.get(config_set, "service_region", fallback=config.get("Azure", "service_region", fallback=""))

        if not azure_key or not service_region:
            print(f"An error occurred. Invalid azure key or service region in {os.path.abspath(CONFIG_FILE_PATH)}.")
            raise ValueError("Invalid azure key or service region.")
        
        self.speech_config = speechsdk.SpeechConfig(subscription=azure_key, region=service_region)
        speech_config_options = SPEECH_CONFIG_OPTIONS.get(config_set, SPEECH_CONFIG_OPTIONS["aria"]
                                                        )
        for option, value in speech_config_options.items():
            setattr(self.speech_config, f"speech_synthesis_{option}", value)
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config)

    def synthesize_text(self, text):
        """Synthesize text and return the audio data."""
        # Perform speech synthesis asynchronously and get the result
        result = self.speech_synthesizer.speak_text_async(text).get()
        # Check if the result is successful
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            # Return the audio data as bytes
            return result.audio_data
        else:
            # Print an error message with the result status
            print(f"An error occurred. Speech synthesis status: {result.reason}")
            # Return None
            return None
        
if __name__ == "__main__":
    tts = TextToSpeech()

    text = """
    Hello. I love cheetos. That is all.
    """

    audio_data = tts.synthesize_text(text)
    print(f"Audio data type: {type(audio_data)}, length: {len(audio_data)}")