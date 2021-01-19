class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ml = -1
        d = {}
        for i, c in enumerate(s):
            start = d.setdefault(c, i + 1)
            ml = max(ml,i - start)
        return ml     