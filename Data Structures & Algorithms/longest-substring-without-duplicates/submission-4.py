class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        seen={}
        res=0
        for j in range(len(s)):
            if s[j] in seen:
                i=max(seen[s[j]]+1, i)
            seen[s[j]]=j
            res=max(res, j-i+1)
        return res