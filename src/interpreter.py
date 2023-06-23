from .layer import Layer


def interpret(layer: Layer):
    """Converts a layer model into a dataframe with relevant song information."""
    beats_per_minute = layer.beats_per_minute
    return [beats_per_minute]


def orchestrate(layers):
    """Synthesizes data on individual layers into data about the entire song."""
    raise NotImplementedError
