import os
import pickle
from sklearn.cluster import KMeans

from .interpreter import Interpreter
from .isolator import Isolator
from .layer import Layer

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
        self.interpreter = Interpreter()
        self.model = load_model()
        self.jobs = 0

    def add(self, song):
        """Converts song into relevant data, then adds it to the library."""
        # temporarily, only handle songs with one instrument layer
        # layers = map(Layer, self.isolator.isolate(song))
        # data_per_layer = map(self.interpreter.interpret, layers)
        # data = self.interpreter.orchestrate(data_per_layer)
        layer_filename = f'temp/{self.jobs}.mp3'
        self.jobs += 1

        with open(layer_filename, 'wb') as f:
            f.write(song['file'].encode('utf-8'))

        layer = Layer(layer_filename)
        os.remove(layer_filename)
        data = self.interpreter.interpret(layer)
        self.model = self.model.partial_fit(data)
        pickle.dump(self.model, open(MODEL_FILENAME, 'wb'))
        print(layer.note_sequence)

    def recommend(self, params):
        """Recommends a particular amount of songs based on user's past listening experiences."""
        raise NotImplementedError
