from seed import Seed


class Vault:
    def __init__(self):
        self._seeds = set()
        self._counter = 0

    def store(self, seed):
        self._counter += 1
        seed.id = self._counter
        self._seeds.add(seed)
        return seed

    def seeds(self):
        return set(self._seeds)
