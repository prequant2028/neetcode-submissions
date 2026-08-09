class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        freq={}
        res=0
        lim=k
        for j in range(len(s)):
            freq[s[j]]=freq.get(s[j], 0)+1
            lim=(j-i+1)-max(freq.values())
            if lim>k:
                freq[s[i]]-=1
                i+=1
            res=max(res, j-i+1)
        return res