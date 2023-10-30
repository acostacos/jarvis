from parts.ears import Ears
from parts.mouth import Mouth
from parts.brain import Brain

class Jarvis:
    def __init__(self):
        self.name = 'jarvis'
        self.ears = Ears()
        self.mouth = Mouth()
        self.brain = Brain()

    def accept_commands(self):
        input = ''
        while self.name not in input.lower():
            input = self.ears.listen_whisper()
            print(input)

        self.mouth.say('Hello. What do you need?')

        while True:
            input = self.ears.listen_whisper()
            print(input)
            
            if 'thank you' in input.lower():
                break

            answer = self.brain.request_answer(input)
            self.mouth.say(answer)
        
        self.mouth.say("You're welcome. Goodbye.")
