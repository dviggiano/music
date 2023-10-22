import numpy as np


class Model:
    def __init__(self):
        self.data = None

    def fit(self, data):
        self.data = np.array(data)

    def append(self, data):
        row = np.array([data])
        self.data = np.vstack((self.data, row))

    def recommend(self, x, count):
        return sorted(self.data, key=lambda x2: np.linalg.norm(x - x2))[:count]
