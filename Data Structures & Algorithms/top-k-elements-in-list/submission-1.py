class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = [[] for i in range(len(nums) + 1)]
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1

        for n, c in counts.items():
            result[c].append(n)
        
        res = []

        for i in range(len(result) - 1, 0, -1):
            for n in result[i]:
                res.append(n)
            
                if len(res) == k:
                    return res

        