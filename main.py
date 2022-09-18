import speech_recognition as sr
import helper_functions as helper


def main():
    recognizer = sr.Recognizer()
    pyaudio = sr.Microphone.get_pyaudio().PyAudio()
    microphone = helper.get_default_mic(pyaudio)

    while True:
        voice_audio = helper.listen(microphone, recognizer)
        voice_text = helper.translate_voice_to_text(voice_audio, recognizer)

        # Get first word that is picked up
        # Pass that word to processing command
        # Pass rest of the sentence as arguments

        # Process commands


main()
