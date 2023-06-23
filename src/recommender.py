import os
import pickle
from sklearn.cluster import KMeans
from flask import FileStorage

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

    def add(self, song: FileStorage):
        """Converts song into relevant users, then adds it to the library."""
        # temporarily, only handle songs with one instrument layer
        # layers = map(Layer, self.isolator.isolate(song))
        # data_per_layer = map(self.interpreter.interpret, layers)
        # users = self.interpreter.orchestrate(data_per_layer)
        temp_filename = f'{self.jobs}.mp3'
        self.jobs += 1
        song.save(os.path.join('temp', temp_filename))
        layer = Layer(temp_filename)
        os.remove(temp_filename)
        data = self.interpreter.interpret(layer)
        self.model = self.model.partial_fit(data)
        pickle.dump(self.model, open(MODEL_FILENAME, 'wb'))
        return {
            'name': song.filename.rstrip('.mp3'),
            'length': layer.duration,
        }

    def recommend(self, params):
        """Recommends a particular amount of songs based on user's past listening experiences."""
        return ['' for _ in range(params['amount'])]
