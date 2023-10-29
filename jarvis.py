from parts.ears import Ears
from parts.mouth import Mouth

class Jarvis:
    def __init__(self, language):
        self.name = 'jarvis'
        self.ears = Ears()
        self.mouth = Mouth(language)

    def accept_commands(self):
        input = ''
        while self.name not in input.lower():
            input = self.ears.listen_whisper()

        self.mouth.say('Hello. What do you need?')
