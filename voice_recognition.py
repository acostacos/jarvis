import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=2)
with mic as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)

text = ""
try:
    text = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Unable to recognize audio")
except:
    print("Error")

print(text)
print(sr.__version__)
print(sr.Microphone.list_microphone_names())
