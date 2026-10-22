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
            j = s.find("#", i)             
            length = int(s[i:j])   
            word = s[j+1:j + length +1 ]           
            result.append(word)
            i = j + 1 + length                       
        return result
