from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        
        for num in nums_set:
            seq=0
            if num - 1 not in nums_set:
                for i in range(len(nums)):
                    if num+i in nums_set:
                        seq+=1
                    else:
                        break
            res=max(seq, res)
        return res