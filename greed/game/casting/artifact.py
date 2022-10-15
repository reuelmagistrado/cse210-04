from game.casting.actor import Actor


class Artifact(Actor):
    """A visible, moving thing that participates in the game. 

    The responsibility of Artifact is to keep track of points of gems and stones.

    Attributes:
        _points: The points of gems and stones.
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._points = 0

    def get_points(self):
        """Gets the artifact's point.

        Returns:
            Points: The artifact's equivalent point.
        """
        if (self.get_text() == '*'):
            self._points = 1
        else:
            self._points = -1

        return self._points
