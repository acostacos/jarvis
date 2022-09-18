import speech_recognition as sr

recognizer = sr.Recognizer()

pyaudio = sr.Microphone.get_pyaudio().PyAudio()
default_mic = pyaudio.get_default_input_device_info()
# Handle if default mic is not available - throws IOError

device_index = default_mic.get('index')
mic = sr.Microphone(device_index=dev_idx)
with mic as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    audio = recognizer.listen(source)

text = ""
try:
    text = recognizer.recognize_google(audio)
except sr.UnknownValueError:
    print("Unable to recognize audio")
except:
    print("Error")

print(text)
