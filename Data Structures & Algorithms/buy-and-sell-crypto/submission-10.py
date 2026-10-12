class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        start = 0
        end = 1

        while end < len(prices):
            if prices[start] > prices[end]:
                start = end
                end += 1
            else:
                max_sum = max(max_sum, prices[end] - prices[start])
                end += 1
        
        return max_sum
        