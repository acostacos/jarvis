import speech_recognition as sr

class Ears:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone() # Gets default microphone
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

    def listen_whisper(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)

        try:
            return self.recognizer.recognize_whisper(audio)
        except sr.UnknownValueError:
            return "Unable to recognize audio."
        except Exception as e:
            print(e) 
            return "An unknown error occurred."
