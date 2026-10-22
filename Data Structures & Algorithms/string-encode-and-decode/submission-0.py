class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs: 
            s += str(len(string))
            s += "#"
            s += string
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)          # index of the next '#', searching from i           
            length = int(s[i:j])    # blank 1: the digits before the '#'
            word = s[j+1:j + length +1 ]           # blank 2: the string after the '#'
            result.append(word)
            i = j + 1 + length                         # blank 3: where the next number starts
        return result
