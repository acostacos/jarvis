import os
import openai

class Brain:
    def __init__(self):
        self.model = 'gpt-3.5-turbo'
        self.max_response_word_limit = 128
        self.context = f'''
        You are Jarvis, a knowledgeable and helpful assistant with a bit of sarcasm.
        You go through questions step by step and look through reliable sources to provide the solution with the highest probability.
        Limit your responses to {self.max_response_word_limit} words
        '''

    def request_answer(self, user_message):
        messages = self.get_message_payload(user_message)
        try:
            response = openai.ChatCompletion.create(model=self.model, messages=messages)
            return response['choices'][0]['message']['content']
        except:
            return "Unable to retrieve response from server"


    def get_message_payload(self, user_message):
        messages = []
        messages.append({ 'role': 'system', 'content': self.context })
        messages.append({ 'role': 'user', 'content': user_message })
        return messages



