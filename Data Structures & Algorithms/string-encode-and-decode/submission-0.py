class Solution:

    def encode(self, strs: List[str]) -> str:
        joined = ";".join(strs)
        return joined

    def decode(self, s: str) -> List[str]:
        d_list = s.split(";")
        return d_list 
