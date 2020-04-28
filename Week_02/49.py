from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for i in strs:
            m[tuple(sorted(i))].append(i)

        return list(m.values())
