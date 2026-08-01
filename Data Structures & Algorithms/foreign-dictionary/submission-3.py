class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        rules = {j:set() for i in words for j in i}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            for index in range(minLen):
                if w1[index] != w2[index]:
                    rules[w1[index]].add(w2[index])
                    break
                    
        
        print(rules)

        visit = {} #False means visited but not in current path, True means visited and in current path
        result = []
        def dfs(letter):
            if letter in visit:
                return visit[letter]
            visit[letter] = True
            for nei in rules[letter]:
                if dfs(nei):
                    return True
            visit[letter] = False
            result.append(letter)
        
        for letter in rules:
            if dfs(letter):
                return ""
        result.reverse()
        return "".join(result)