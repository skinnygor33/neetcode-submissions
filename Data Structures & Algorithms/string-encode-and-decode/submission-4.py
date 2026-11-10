class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s))
            string += "#"
            string += s
        return string 

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = 0
        while j != len(s):
            while s[j] != "#": 
                j += 1
            lenght = int(s[i:j])
            i = j + 1
            j = i + lenght
            result.append(s[i:j])
            i = j 
        return result

        """
        5#Hello5#World
                 i
                     j

        """

