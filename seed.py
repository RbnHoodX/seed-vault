class Seed:
    def __init__(self, name=""):
        self.id = 0
        self.name = name
        self._phase = "dormant"

    @property
    def phase(self):
        return self._phase

    def __eq__(self, other):
        if not isinstance(other, Seed):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"Seed(id={self.id}, name={self.name!r})"
