import pyttsx3

class Mouth:
    def __init__(self, language):
        self.engine = pyttsx3.init() 
        self.engine.setProperty('voice', language)
    
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
