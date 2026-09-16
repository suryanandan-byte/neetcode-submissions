class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        l=collections.defaultdict(list)
        for i in s:
            n="".join(sorted(i))
            l[n].append(i)
        return list(l.values())