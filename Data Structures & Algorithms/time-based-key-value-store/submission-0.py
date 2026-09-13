class TimeMap:

    def __init__(self):
        self.store = {}
    
    def find_timestamp(self, key: str, timestamp: int) -> int:
        timestamps = list(self.store[key].keys())
        timestamps.sort()

        left = 0
        right = len(timestamps) - 1
        res = -1

        while left <= right:
            middle = (left + right) // 2

            if timestamps[middle] <= timestamp:
                res = timestamps[middle]
                left = middle + 1
            else:
                right = middle - 1

        return res

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}

        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        t = self.find_timestamp(key, timestamp)

        if t == -1:
            return ""

        return self.store[key][t]