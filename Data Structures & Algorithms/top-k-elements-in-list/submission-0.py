from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen=defaultdict(int)
        for n in nums:
            seen[n]+=1
        buckets = [[] for _ in range(len(nums)+1)]
        for m in seen:
            buckets[seen[m]].append(m)
        
        res = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res