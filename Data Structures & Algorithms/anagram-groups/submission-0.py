from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            seen[key].append(word)
        return list(seen.values())