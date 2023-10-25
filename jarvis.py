from parts.ears import Ears
from parts.mouth import Mouth

class Jarvis:
    def __init__(self, language):
        self.name = 'jarvis'
        self.ears = Ears()
        self.mouth = Mouth(language)

    def listen_for_name(self):
        input = self.ears.listen()
        if (input == self.name):
            self.mouth.say('Hello. What do you need?')

    def say(self, text):
        self.mouth.say(text)
