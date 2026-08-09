class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check(a, b):
            subfreq = {}
            for i in range(a, b+1):
                subfreq[s2[i]] = subfreq.get(s2[i], 0) + 1
            return subfreq == s1freq
        i=0
        j=len(s1)-1
        s1freq={}
        for m in s1:
            s1freq[m]=s1freq.get(m, 0)+1
        while j<len(s2):
            if not check(i, j):
                i+=1
                j+=1
            else:
                return True
        return False