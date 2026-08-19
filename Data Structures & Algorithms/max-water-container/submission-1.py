class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_total = 0
        pair = (0, heights[len(heights) - 1] )

        start, end = 0, len(heights) - 1

        while end > start:
            temp_min = min(heights[start], heights[end])
            temp_max = temp_min * (end - start)

            max_total = max(temp_max, max_total)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return max_total

                
        