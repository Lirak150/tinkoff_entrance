class Cell:
    def __init__(self, is_alive):
        self._is_alive = is_alive

    def __str__(self):
        return 'x' if self.is_alive else ' '

    def make_dead(self):
        self._is_alive = False

    def make_alive(self):
        self._is_alive = True

    def num_repr(self):
        return 1 if self.is_alive else 0

    @property
    def is_alive(self):
        return self._is_alive

    def __eq__(self, other):
        if not isinstance(other, Cell):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.is_alive == other.is_alive
