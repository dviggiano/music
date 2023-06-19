from .layer_model import LayerModel


class Interpreter:
    def __init__(self):
        raise NotImplementedError

    def interpret(self, layer: LayerModel):
        """Converts a layer model into a dataframe with relevant song information."""
        raise NotImplementedError

    def orchestrate(self, layers):
        """Synthesizes data on individual layers into data about the entire song."""
        raise NotImplementedError
