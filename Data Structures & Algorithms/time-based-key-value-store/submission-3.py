class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

        

    def get(self, key: str, timestamp: int) -> str:

        if not key in self.store:
            return ""
    

        vals = self.store[key]
        left = 0
        right = len(vals) - 1
        res = ""

        while left <= right:
            mid = (left+right)//2


            if vals[mid][1] <= timestamp and abs(vals[mid][1] - timestamp) <= abs(vals[mid][1] - timestamp):
                res = vals[mid][0]

            if vals[mid][1] > timestamp:
                right = mid - 1
            elif vals[mid][1] == timestamp:
                return vals[mid][0]
            else:
                # vals[mid][1] less than target
                # if abs(vals[mid][1] - timestamp) <= abs(vals[mid][1] - timestamp):
                #     res = vals[mid][1]
                left = mid + 1
        
        return res


        

        
