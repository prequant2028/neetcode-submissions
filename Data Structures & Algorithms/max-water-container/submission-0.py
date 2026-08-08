class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        vol=0
        while i<j:
            v=(j-i)*min(heights[i], heights[j])
            vol=max(v, vol)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return vol