class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""

        for i in range(len(s)):
            if s[i].isalnum():
                new_string += s[i].lower()
        
        return new_string == new_string[::-1]
        