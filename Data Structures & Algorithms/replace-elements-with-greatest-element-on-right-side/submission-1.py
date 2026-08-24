class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        max_right=0
        for i in range(n-1, -1, -1):
            cur=arr[i]
            if i<n-1:
                arr[i]=max_right
            else:
                arr[i]=-1
            max_right=max(max_right, cur)
        return arr