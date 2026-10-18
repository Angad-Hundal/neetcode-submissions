class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # hash from sort to list
        # sort each element
        # and if key in hash
        # add it 
        # else make a new list

        # then combine all the lists together

        def create_hash(strs: List[str]):
            hash = {}

            for idx, value in enumerate(strs):
                key = "".join(sorted(value))
                if key in hash:
                    hash[key].append(value)
                else:
                    hash[key] = [value]
            
            return hash
        
        def combine(hash):
            result = []

            for key, value in hash.items():
                result.append(value)
            return result

        hash = create_hash(strs)
        return combine(hash)




        