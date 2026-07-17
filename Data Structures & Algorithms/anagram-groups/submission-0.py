from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}

        for st in strs:
            key = ''.join(sorted(st))

            if key not in grp:
                grp[key] = []

            grp[key].append(st)

        return list(grp.values())