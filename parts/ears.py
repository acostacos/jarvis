import speech_recognition as sr

class Ears:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone() # Gets default microphone
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

    def listen(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)

        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Unable to recognize audio."
        except:
            return "An unknown error occurred."