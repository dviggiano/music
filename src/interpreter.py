from .layer import Layer


class Interpreter:
    def __init__(self):
        pass

    def interpret(self, layer: Layer):
        """Converts a layer model into a dataframe with relevant song information."""
        raise NotImplementedError

    def orchestrate(self, layers):
        """Synthesizes data on individual layers into data about the entire song."""
        raise NotImplementedError
