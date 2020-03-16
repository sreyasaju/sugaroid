"""
MIT License

Sugaroid Artificial Inteligence
Chatbot Core
Copyright (c) 2020 Srevin Saju

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from chatterbot.logic import LogicAdapter
from sugaroid.brain.wiki import WikiAdapter

from sugaroid.brain.preprocessors import normalize

from sugaroid.brain.postprocessor import random_response

from sugaroid.brain.constants import WHY_IDK
from sugaroid.brain.ooo import Emotion
from sugaroid.sugaroid import SugaroidStatement


class WhyWhenAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        # FIXME Add Language support
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.tokenized = self.chatbot.lp.tokenize(str(statement))
        self.normalized = normalize(str(statement))
        for i in self.tokenized:
            if i.tag_ == 'WRB':
                return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        """

        :param statement:
        :param additional_response_selection_parameters:
        :return:
        """
        emotion = Emotion.neutral
        if 'when' in self.normalized:
            # search in wikipedia
            return WikiAdapter(self.chatbot).process(statement)
        elif 'why' in self.normalized:
            # say idk
            response = random_response(WHY_IDK)
            confidence = 0.2
            emotion = Emotion.cry_overflow
        else:
            # say idk
            response = ':)'
            confidence = 0.15
        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = confidence
        selected_statement.emotion = emotion

        return selected_statement