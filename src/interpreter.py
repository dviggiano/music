from .layer import Layer

FEATURES = [
    'bpm',
]


def interpret(layer: Layer):
    """Converts a layer model into a dataframe with relevant song information."""
    beats_per_minute = layer.beats_per_minute
    # TODO perform musical analysis to extract more features (key, patterns...)
    return [beats_per_minute]


def orchestrate(layers: list[Layer]):
    """Synthesizes data on individual layers into data about the entire song."""
    raise NotImplementedError
