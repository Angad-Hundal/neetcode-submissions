from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = OrderedDict()

    def get(self, key: int) -> int:

        if key not in self.store:
            return -1

        # Move key to the most recently used position
        self.store.move_to_end(key)

        return self.store[key]

    def put(self, key: int, value: int) -> None:

        if key in self.store:
            self.store.move_to_end(key)

        self.store[key] = value

        if len(self.store) > self.capacity:
            # Remove least recently used (first item)
            self.store.popitem(last=False)