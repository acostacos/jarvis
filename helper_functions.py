import speech_recognition as sr


def get_default_mic(pyaudio):
    default_mic = pyaudio.get_default_input_device_info()
    # Handle if default mic is not available - throws IOError

    dev_idx = default_mic.get('index')
    return sr.Microphone(device_index=dev_idx)


def listen(microphone, recognizer):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    return audio


def translate_voice_to_text(audio, recognizer):
    text = ""
    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Unable to recognize audio")
    except:
        print("Error")
    return text
