class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        total = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                total = max(total, prices[right] - prices[left])
            right += 1
        return total
        