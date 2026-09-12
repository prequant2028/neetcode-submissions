class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        up=max(piles)
        l=1
        r=up
        while l<r:
            k=(l+r)//2
            m=0
            for i in range(len(piles)):
                m+=(piles[i] + k - 1) // k
            if m>h:
                l=k+1
            elif m<=h:
                r=k
        return l