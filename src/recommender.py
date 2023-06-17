import os
import pickle
from sklearn.cluster import KMeans

from .interpreter import Interpreter
from .isolator import Isolator
from .transformer import Transformer

MODEL_FILENAME = 'model.sav'
NUM_CLUSTERS = 8


def load_model():
    if os.path.exists(MODEL_FILENAME):
        return pickle.load(open(MODEL_FILENAME, 'rb'))

    model = KMeans(n_clusters=NUM_CLUSTERS)
    # TODO train using saved song library
    pickle.dump(model, open(MODEL_FILENAME, 'wb'))
    return model


class Recommender:
    def __init__(self):
        self.isolator = Isolator()
        self.transformer = Transformer()
        self.interpreter = Interpreter()
        self.model = load_model()

    def add(self, song):
        """Converts song into relevant data, then adds it to the library."""
        # temporarily, only handle songs with one instrument layer
        # sheet_music = map(self.transformer.layer_to_sheet, self.isolator.isolate(song))
        # data_per_layer = map(self.interpreter.interpret, sheet_music)
        # data = self.interpreter.orchestrate(data_per_layer)
        sheet_music = self.transformer.layer_to_sheet(song['file'])
        data = self.interpreter.interpret(sheet_music)
        self.model = self.model.partial_fit(data)
        pickle.dump(self.model, open(MODEL_FILENAME, 'wb'))

    def recommend(self, params):
        """Recommends a particular amount of songs based on user's past listening experiences."""
        raise NotImplementedError
