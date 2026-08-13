class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights)):
            h = heights[i]
            if i > 0 and h == heights[i-1]:
                continue

            j = i - 1
            k = i + 1

            while j > -1 and heights[j] >= h:
                j -= 1

            while k < len(heights) and heights[k] >= h:
                k += 1

            area = h * (k - j - 1)
            res = max(res, area)

        return res