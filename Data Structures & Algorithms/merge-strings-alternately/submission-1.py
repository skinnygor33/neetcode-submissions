class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        lenght = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range(0, lenght):
            result += word1[i]
            result += word2[i]
        
        if len(word1) < len(word2):
            result += word2[i+1:]
            print("hello")
            return result 
        elif len(word2) < len(word1):
            result += word1[i+1:]
            return result 
        else: 
            return result 
