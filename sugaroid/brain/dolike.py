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


import nltk
from chatterbot.logic import LogicAdapter
from sugaroid.brain.ooo import Emotion
from sugaroid.sugaroid import SugaroidStatement


class DoLikeAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.normalized = False

    def can_process(self, statement):
        self.normalized = nltk.word_tokenize(str(statement).lower())
        if 'do' in self.normalized and 'like' in self.normalized:
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        emotion = Emotion.neutral
        response = 'ok'
        confidence = 0



        selected_statement = SugaroidStatement(response)
        selected_statement.confidence = confidence

        selected_statement.emotion = emotion
        return selected_statement
