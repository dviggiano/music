class Interpreter:
    def __init__(self):
        raise NotImplementedError

    def interpret(self, music):
        """Converts sheet music into a dataframe with relevant song information."""
        raise NotImplementedError

    def coalesce(self, layers):
        """Converts data on individual layers into data about the entire song."""
        raise NotImplementedError
