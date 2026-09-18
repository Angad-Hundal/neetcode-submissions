class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:

        for item in self.cache:

            if item[0] == key:
                self.cache.remove(item)
                self.cache.append(item)

                return item[1]

        return -1

    def put(self, key: int, value: int) -> None:

        # If key already exists
        for item in self.cache:

            if item[0] == key:
                self.cache.remove(item)
                item[1] = value
                self.cache.append(item)

                return

        # If cache is full
        if len(self.cache) == self.capacity:
            self.cache.pop(0)

        # Add as most recently used
        self.cache.append([key, value])