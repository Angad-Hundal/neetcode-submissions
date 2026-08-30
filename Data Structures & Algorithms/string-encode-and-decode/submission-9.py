class Solution:

    def encode(self, strs: List[str]) -> str:

        final = ""
        for value in strs:
            final +=  str(len(value)) + "#" + value
        return final


    # check all the chars
    # if char at index is float and char's next index is #
    # append the i + 2: index +2 + int(char) in the final list

    # for bigger words like 12#
    # get the first number: check for the index of #
    # anything before than is the length of the first string
    # and anything after the # and number length is the first string
    # then again check for another # and repeat the process
    # while string exists

    def decode(self, s: str) -> List[str]:

        if s == "":
            return []
    
        
        final = []

        while s:

            hash_index = s.find("#")

            if hash_index == -1:
                return final.append(s)

            len_number = s[:hash_index]
            final.append(s[hash_index+1:hash_index+1+int(len_number)])
            s = s[hash_index+1+int(len_number): ]
        
        return final
        
        

        
        
