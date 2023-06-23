import csv
import os
import pickle
from sklearn.cluster import KMeans
from werkzeug.datastructures import FileStorage

from .interpreter import Interpreter
from .isolator import Isolator
from .layer import Layer

SONG_DATA_FILENAME = 'songs.csv'
USER_DATA_FILENAME = 'users.csv'
MODEL_FILENAME = 'model.sav'
NUM_CLUSTERS = 8


def load_songs():
    try:
        with open(SONG_DATA_FILENAME, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header
            return list(reader)
    except FileNotFoundError:
        return []


def load_model():
    if os.path.exists(MODEL_FILENAME):
        return pickle.load(open(MODEL_FILENAME, 'rb'))

    model = KMeans(n_clusters=NUM_CLUSTERS)
    # TODO train using saved song library
    pickle.dump(model, open(MODEL_FILENAME, 'wb'))
    return model


def save_song(data):
    csv_exists = os.path.isfile(SONG_DATA_FILENAME)

    with open(SONG_DATA_FILENAME, 'a') as f:
        writer = csv.writer(f)

        if not csv_exists:
            writer.writerow(['name', 'length'])

        writer.writerow(data)


class Engine:
    def __init__(self):
        self.isolator = Isolator()
        self.interpreter = Interpreter()
        self.model = load_model()
        self.songs = load_songs()
        self.jobs = 0

    def add(self, song: FileStorage):
        """Converts song into relevant data, then adds it to the library."""
        # temporarily, only handle songs with one instrument layer
        # layers = map(Layer, self.isolator.isolate(song))
        # data_per_layer = map(self.interpreter.interpret, layers)
        # users = self.interpreter.orchestrate(data_per_layer)
        temp_filename = os.path.abspath(f'temp/{self.jobs}.mp3')
        self.jobs += 1
        song.save(temp_filename)
        layer = Layer(temp_filename)
        os.remove(temp_filename)
        print(layer.note_sequence)
        data = self.interpreter.interpret(layer)
        self.model = self.model.partial_fit(data)
        entry = {'name': song.filename.rstrip('.mp3'), 'length': layer.duration}
        save_song(entry.values())
        self.songs.append(entry.values())
        pickle.dump(self.model, open(MODEL_FILENAME, 'wb'))
        return entry

    def recommend(self, params):
        """Recommends a particular amount of songs based on user's past listening experiences."""
        _ = self
        return ['' for _ in range(params['amount'])]
