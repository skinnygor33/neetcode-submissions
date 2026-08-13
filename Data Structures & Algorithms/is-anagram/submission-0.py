class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}

        for i in range(0, len(t)):
            hashmap[t[i]] = hashmap.get(t[i], 0) + 1
        for i in range(0, len(s)):
            if s[i] not in hashmap or hashmap[s[i]] == 0:
                return False
            hashmap[s[i]] -= 1

        return True