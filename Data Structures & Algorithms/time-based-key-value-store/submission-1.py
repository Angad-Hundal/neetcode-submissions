class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if not key in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        if not key in self.store:
            return ""
        
        # timestamp in ascending order

        left = 0
        right = len(self.store[key]) - 1
        value = ""
        closest = -1

        while left <= right:
            middle = (left + right) // 2

            num_middle = self.store[key][middle][1]

            if num_middle > timestamp:
                right = middle - 1

                if timestamp - num_middle < timestamp - closest:
                    value = self.store[key][middle][0]
                    closest = self.store[key][middle][1]

            elif num_middle < timestamp:
                left = middle + 1

                if timestamp - num_middle < timestamp - closest:
                    value = self.store[key][middle][0]
                    closest = self.store[key][middle][1]

            else:
                return self.store[key][middle][0] 
        
        return value
        
