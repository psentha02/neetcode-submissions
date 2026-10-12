class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in characters:
                characters.remove(s[l])
                l += 1
            characters.add(s[r])
            max_len = max(max_len, len(characters))

        return max_len
        