class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity


    def get(self, key: int) -> int:

        # pop the array
        # return the value
        # append it at back

        for idx, val_array in enumerate(self.cache):
            if val_array[0] == key:
                popped_array = self.cache.pop(idx)
                self.cache.append(popped_array)
                return popped_array[1]
        
        return -1


    def put(self, key: int, value: int) -> None:

        for idx, val_array in enumerate(self.cache):
            if val_array[0] == key:
                popped_array = self.cache.pop(idx)
                popped_array[1] = value
                self.cache.append(popped_array)
                return
        
        if self.capacity == len(self.cache):
            self.cache.pop(0)
        
        self.cache.append([key, value])

        