class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {} # key -> value
        self.order = [] # the keys in order
        

    def get(self, key: int) -> int:
        
        if key not in self.store:
            return -1
        
        self.order.remove(key)
        self.order.append(key)

        return self.store[key]

        

    def put(self, key: int, value: int) -> None:
        
        if key in self.store:
            self.order.remove(key)
        

        self.store[key] = value
        
        self.order.append(key)

        if len(self.store) > self.capacity:
            e = self.order.pop(0)
            del self.store[e]
        


        
