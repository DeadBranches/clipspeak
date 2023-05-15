# Set up different configuration sets
config_sets = ["aria", "grace", "invalid"]
# Test if TextToSpeech initializes correctly with each configuration set
for config_set in config_sets:
    # Create a TextToSpeech object with the given configuration set
    tts = speech.TextToSpeech(config_set=config_set)
    # Check if the speech config and synthesizer objects are created correctly
    mock_speech_config.assert_called_once()
    mock_speech_synthesizer.assert_called_once_with(speech_config=mock_speech_config.return_value)
    # Reset the mocks for the next iteration
    mock_speech_config.reset_mock()
    mock_speech_synthesizer.reset_mock()

@mock.patch("speechsdk.SpeechSynthesizer")
@mock.patch("speechsdk.SpeechConfig")
def test_synthesize_text(self, mock_speech_config, mock_speech_synthesizer):
    """Test if TextToSpeech synthesizes text correctly with different texts."""
    # Set up different texts
    texts = ["Hello", "123", "", "ClipSpeak"]
    # Set up different audio data
    audio_data = [b"audio1", b"audio2", b"audio3", b"audio4"]
    # Set up the mock speech synthesizer to return different results
    mock_speech_synthesizer.return_value.speak_text_async.side_effect = [
        mock.Mock(reason=speechsdk.ResultReason.SynthesizingAudioCompleted, audio_data=data) for data in audio_data
    ]
    # Create a TextToSpeech object with the default configuration set
    tts = speech.TextToSpeech()
    # Test if TextToSpeech synthesizes text correctly with each text
    for i, text in enumerate(texts):
        # Call the synthesize_text method with the given text
        result = tts.synthesize_text(text)
        # Check if the speech synthesizer is called correctly with the given text
        mock_speech_synthesizer.return_value.speak_text_async.assert_called_once_with(text)
        # Check if the result is the same as the expected audio data
        self.assertEqual(result, audio_data[i])
        # Reset the mock for the next iteration
        mock_speech_synthesizer.return_value.speak_text_async.reset_mock()

if __name__ == "__main__":
    unittest.main()
