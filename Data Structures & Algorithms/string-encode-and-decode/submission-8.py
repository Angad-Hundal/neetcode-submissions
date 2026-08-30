class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1 and (strs[0] == ""):
            return ""
        elif len(strs) == 0:
            return []
        joined = ";".join(strs)
        return joined

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        elif s == None:
            return []
        d_list = s.split(";")
        return d_list 
