import csv
import os
import pickle
from werkzeug.datastructures import FileStorage

from .constants import SONG_LIST_FILENAME, SONG_DATA_FILENAME, MODEL_FILENAME
from .model import Model
from .interpreter import FEATURES, interpret, orchestrate
from .isolator import Isolator
from .layer import Layer


def load_songs():
    if os.path.exists(SONG_LIST_FILENAME):
        with open(SONG_LIST_FILENAME, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header
            return list(reader)

    return []


def load_model():
    if not os.path.exists(SONG_DATA_FILENAME):
        with open(SONG_DATA_FILENAME, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(FEATURES)

    with open(SONG_DATA_FILENAME, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip the header
        data = [row for row in reader if len(row) > 0]

    if os.path.exists(MODEL_FILENAME):
        model = pickle.load(open(MODEL_FILENAME, 'rb'))
    else:
        model = Model()

        if data:
            model.fit(data)
            pickle.dump(model, open(MODEL_FILENAME, 'wb'))

    return model, data


class Engine:
    def __init__(self):
        self.isolator = Isolator()
        self.model, self.song_data = load_model()
        self.song_list = load_songs()
        self.jobs = 0

    def add(self, song: FileStorage):
        """Converts song into relevant data, then adds it to the library."""
        # temporarily, only handle songs with one instrument layer
        # layers = map(Layer, self.isolator.isolate(song))
        # data_per_layer = map(self.interpreter.interpret, layers)
        # data = orchestrate(data_per_layer)
        temp_filename = os.path.abspath(f'temp/{self.jobs}.mp3')
        self.jobs += 1
        song.save(temp_filename)
        layer = Layer(temp_filename)
        os.remove(temp_filename)
        data = interpret(layer)
        self.train(data)
        entry = {'name': song.filename.rstrip('.mp3'), 'duration': layer.duration}
        self.save_song(entry.values())
        return entry

    def train(self, data):
        self.song_data.append(data)
        self.model.append(self.song_data)

        csv_exists = os.path.isfile(SONG_DATA_FILENAME)

        with open(SONG_DATA_FILENAME, 'a') as f:
            writer = csv.writer(f)

            if csv_exists:
                writer.writerow(data)
            else:
                writer.writerow(FEATURES)
                map(writer.writerow, self.song_data)

        pickle.dump(self.model, open(MODEL_FILENAME, 'wb'))

    def save_song(self, data):
        csv_exists = os.path.isfile(SONG_LIST_FILENAME)

        with open(SONG_LIST_FILENAME, 'a') as f:
            writer = csv.writer(f)

            if not csv_exists:
                writer.writerow(['name', 'duration'])

            writer.writerow(data)

        self.song_list.append(data)

    def recommend(self, params):
        """Recommends a particular amount of songs based on user's past listening experiences."""
        # TODO based on user's listening sessions
        #   project some points where they might be interested and find nearest neighbors
        raise NotImplementedError
