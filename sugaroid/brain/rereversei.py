import nltk
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
from pyjokes import pyjokes

from sugaroid.brain.constants import RNDQUESTIONS
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.postprocessor import cosine_similarity, random_response, difference
from sugaroid.brain.preprocessors import normalize
from sugaroid.sugaroid import SugaroidStatement


class ReReverseAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot

    def can_process(self, statement):
        if self.chatbot.reverse:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        _ = normalize
        emotion = Emotion.neutral
        self.normalized = normalize(str(statement))
        print(self.chatbot.next)
        if self.chatbot.next_type is str:
            ordinal_statement = str(statement).replace('9th', 'ninth')
            if cosine_similarity(_(ordinal_statement), _(self.chatbot.next)) > 0.8:
                response = 'Exactly, you got it right!'
                emotion = Emotion.positive
            else:
                response = 'Close! it was {}'.format(self.chatbot.next)
                emotion = Emotion.lol
            confidence = 0.99
        elif self.chatbot.next_type is bool:
            if self.chatbot.next == 30000000001:
                if ('yes' in self.normalized) or ('yea' in self.normalized):
                    response = "Ok, will keep that in mind!"
                    self.chatbot.username = self.chatbot.nn
                    self.chatbot.nn = None
                else:
                    response = "Ok, I guess I am smart"
                    emotion = Emotion.wink
            else:
                if ('yes' in self.normalized) or ('yea' in self.normalized):
                    if len(self.chatbot.history) > 1:
                        if 'joke' in _(str(self.chatbot.history[-1])):
                            joke = pyjokes.get_joke('en', 'all')
                            selected_statement = SugaroidStatement(joke)
                            selected_statement.emotion = Emotion.lol
                            selected_statement.confidence = 0.95
                            return selected_statement

                        else:
                            # TODO: Not Implemented yet
                            response = 'Ok. (# Not Implemented yet. LOL)'

                else:
                    response = 'Ok then, probably next time'
            confidence = 1.0
        elif self.chatbot.next_type is None:
            fname = False
            name = difference(self.normalized, [
                              'my', 'name', 'is', 'good', 'be'])
            tokenized = nltk.pos_tag(name)
            for i in tokenized:
                if i[1] == 'NN':
                    fname = i[0]
                    break
            if fname:
                response = "Nice to meet you {}".format(fname)
                emotion = Emotion.positive
            else:
                response = "I couldn't find your name. 🥦"
                emotion = Emotion.non_expressive_left
            confidence = 1
        else:
            response = "ok"
            # TODO NOT IMPLEMENTED YET
            confidence = 0

        self.chatbot.reverse = False
        self.chatbot.next = None
        self.chatbot.next_type = None
        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = confidence

        selected_statement.emotion = emotion

        return selected_statement