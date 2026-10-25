class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs: 
            string += str(len(s))
            string += "#"
            string += s
        return string

    def decode(self, s: str) -> List[str]:
        p1 = 0
        p2 = 0
        lenght = 0
        result = []

        while p2 < len(s):
            if s[p2] == "#": 
                lenght = int(s[p1:p2])
                result.append(s[p2+1:p2+1+lenght])
                p1 = p2 + lenght + 1
                p2 = p2 + lenght + 1
            else: 
                p2 += 1
        return result 
