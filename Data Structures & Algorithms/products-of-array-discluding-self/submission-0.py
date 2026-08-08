class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        x=1
        if 0 in nums:
            k=[index for index, value in enumerate(nums) if value==0]
            if len(k)>1:
                res=[0]*len(nums)
            else:
                res=[0]*len(nums)
                for l in k:
                    nums.pop(l)
                for n in nums:
                    x=x*n
                res[k[0]]=x
        else:        
            for n in nums:
                x=x*n

            for m in nums:
                res.append(x//m)
        return res