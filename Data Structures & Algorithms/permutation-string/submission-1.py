class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1freq = {}
        for c in s1:
            s1freq[c] = s1freq.get(c, 0) + 1

        winfreq = {}

        # Build the first complete window
        for c in s2[:len(s1)]:
            winfreq[c] = winfreq.get(c, 0) + 1

        i = 0
        j = len(s1)

        while True:
            if winfreq == s1freq:
                return True

            if j == len(s2):
                break

            # Remove left character
            winfreq[s2[i]] -= 1

            if winfreq[s2[i]] == 0:
                del winfreq[s2[i]]

            i += 1

            # Add new right character
            winfreq[s2[j]] = winfreq.get(s2[j], 0) + 1

            j += 1

        return False