class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        finarr=[0]*n
        for i in range(n-1, -1, -1):
            if i<n-1:
                finarr[i]=max(finarr[i+1], arr[i+1])
            else:
                finarr[i]=-1
        return finarr