class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        start = 0
        end = len(heights) - 1
        while start < end:
            if heights[start] < heights[end]:
                vol = max(vol, heights[start] * (end - start))
                start += 1
            else:
                vol =  max(vol, heights[end] * (end - start))
                end -= 1
        return vol
        