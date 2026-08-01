class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        r = 0

        longest = 0

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                w = r - l + 1
                if w > longest: 
                    longest = w
                
                r += 1
            else:
                chars.remove(s[l])
                l += 1
            
        return longest




        