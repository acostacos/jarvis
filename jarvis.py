from parts.ears import Ears
from parts.mouth import Mouth

class Jarvis:
    def __init__(self, language):
        self.name = 'jarvis'
        self.ears = Ears()
        self.mouth = Mouth(language)

    def accept_commands(self):
        input = None
        while input != self.name:
            input = self.ears.listen()
            print(input)

        self.mouth.say('Hello. What do you need?')
