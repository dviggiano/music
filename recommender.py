from interpreter import Interpreter
from isolator import Isolator
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
        # layers = self.isolator.isolate(song).map(self.transformer.layer_to_sheet).map(self.interpreter.interpret)
        layers = self.transformer.layer_to_sheet.map(self.interpreter.interpret)
        raise NotImplementedError

    def recommend(self, params):
        """Recommends a particular amount of songs based on user's past listening experiences."""
        raise NotImplementedError
