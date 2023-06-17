from src.interpreter import Interpreter
from src.isolator import Isolator
from transformer import Transformer


class Recommender:
    def __init__(self):
        self.isolator = Isolator()
        self.transformer = Transformer()
        self.interpreter = Interpreter()

    def load(self):
        raise NotImplementedError

    def add(self, song):
        """Converts song into relevant data, then adds it to the library."""
        # temporarily, only handle songs with one instrument layer
        # sheet_music = map(self.isolator.isolate(song), self.transformer.layer_to_sheet)
        # data = map(sheet_music, self.interpreter.interpret)
        sheet_music = self.transformer.layer_to_sheet(song['file'])
        data = self.interpreter.interpret(sheet_music)
        raise NotImplementedError

    def recommend(self, params):
        """Recommends a particular amount of songs based on user's past listening experiences."""
        raise NotImplementedError
