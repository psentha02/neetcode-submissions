class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        letters = {
            "2": "abc", 
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(i, curString):
            if len(curString) == len(digits):
                result.append(curString)
                return
            
            for j in letters[digits[i]]:
                backtrack(i+1, curString + j)
        
        if digits:
            backtrack(0, "")
        
        return result


