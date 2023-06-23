from .layer import Layer


class Interpreter:

    def interpret(self, layer: Layer):
        """Converts a layer model into a dataframe with relevant song information."""
        raise NotImplementedError

    def orchestrate(self, layers):
        """Synthesizes users on individual layers into users about the entire song."""
        raise NotImplementedError
