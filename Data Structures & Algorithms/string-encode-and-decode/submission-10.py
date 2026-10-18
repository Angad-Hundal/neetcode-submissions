class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for value in strs:
            result += str(len(value)) + "#" + value
        
        return result


    def decode(self, s: str) -> List[str]:

        res = []

        if s == "":
            return res
        
        while s:
            
            index = s.find("#")

            if index == -1:
                res.append(s)
                return res
            
            length = int(s[:index])

            res.append(s[index + 1: index + length + 1])
            s = s[index+length+1:]
        
        return res

