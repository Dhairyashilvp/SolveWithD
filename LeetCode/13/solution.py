class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        d = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        ans = 0
        for i in range(len(s)):
            if i < l - 1 and d[s[i+1]] > d[s[i]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]
        return ans