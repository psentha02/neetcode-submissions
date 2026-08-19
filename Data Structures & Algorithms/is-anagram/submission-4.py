class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            letters_s[s[i]] = letters_s.get(s[i], 0) + 1
            letters_t[t[i]] = letters_t.get(t[i], 0) + 1

        if letters_s != letters_t:
            return False
        
        return True
