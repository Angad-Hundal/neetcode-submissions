class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs):
            return ""
        joined = ";".join(strs)
        return joined

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        d_list = s.split(";")
        return d_list 
