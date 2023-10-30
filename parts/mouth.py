import pyttsx3

class Mouth:
    def __init__(self):
        self.language='english+f3'

        self.engine = pyttsx3.init() 
        self.engine.setProperty('voice', self.language)
    
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
