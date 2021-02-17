from typing import List, Generator

from chatterbot.conversation import Statement
from spacy.tokens.doc import Doc

from sugaroid.brain.postprocessor import random_response
from sugaroid.brain.preprocessors import tokenize
from sugaroid.brain.utils import LanguageProcessor


lang_processor = LanguageProcessor()


class SugaroidStatement(Statement):
    """
    A modified chatterbot Statement with the additional parameters
    The Chatterbot Statement did not preserve the capabilities to hold
    fundamental data such as name of the adapter and emotion of the statement passed
    The emotion was either a <class 'Emotion'> type or NoneType
    The Adapter was the generic name of the adapter in string type determined
    by the __gtype__ variable
    """

    def __init__(self, text: str, in_response_to=None, emotion: int = None, **kwargs):
        super(SugaroidStatement, self).__init__(text, in_response_to, **kwargs)
        self._doc = lang_processor.nlp(text)
        self._simple = text.rstrip("?,+/.;!").lower().split()
        self._words = tokenize(text)
        self._emotion = emotion
        self.adapter = None
        self.from_chatbot = False

    def set_confidence(self, confidence: float):
        self.confidence = confidence

    def set_emotion(self, emotion: int):
        self.emotion = emotion

    def set_adapter(self, adapter: str):
        self.adapter = adapter

    def set_chatbot(self, is_chatbot: bool):
        self.from_chatbot = is_chatbot

    @property
    def simple(self) -> List[str]:
        """
        Returns the statement stripped and split into words
        :return:
        :rtype:
        """
        return self._simple

    @property
    def tokens(self) -> Doc:
        """
        Alias of self.doc
        :return:
        :rtype:
        """
        return self._doc

    @property
    def doc(self) -> Doc:
        """
        Returns the spacy.tokens.doc.Doc of the statement
        :return:
        :rtype:
        """
        return self._doc

    @property
    def words(self) -> list:
        """
        Returns the normalized words of the statement
        :return:
        :rtype:
        """
        return self._words

    @property
    def lemma(self) -> Generator:
        """
        Returns the normalized words of the statement
        :return:
        :rtype:
        """
        return (x.lemma_ for x in self.doc)

    @property
    def pos(self) -> Generator:
        """
        Returns the pos_ generator words of the statement
        :return:
        :rtype:
        """
        return (x.pos_ for x in self.doc)

    @property
    def tag(self) -> Generator:
        """
        Returns the tag_ generator words of the statement
        :return:
        :rtype:
        """
        return (x.tag_ for x in self.doc)

    @property
    def emotion(self) -> int:
        """
        Gives the assigned emotion of the statement
        :return:
        :rtype:
        """
        return self._emotion

    @emotion.setter
    def emotion(self, new_emotion: int):
        self._emotion = new_emotion

    @classmethod
    def from_statement(cls, statement: Statement):
        """
        Convert chatterbot.Statement to sugaroid.core.statement.Statement
        :param statement:
        :type statement: chatterbot.Statement
        :return:
        :rtype: SugaroidStatement
        """
        return cls(statement.text)

    @classmethod
    def from_list_random(cls, statements: list):
        """
        Select a random statement from a list of statements
        :param statements:
        :type statements:
        :return:
        :rtype: SugaroidStatement
        """
        statement = random_response(statements)
        return cls(statement)