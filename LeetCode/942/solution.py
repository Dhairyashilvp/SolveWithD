class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        mi = 0 
        ma = len(S)
        ans = []
        for e in S:
            if e == "I":
                ans.append(mi)
                mi += 1
            else:
                ans.append(ma)
                ma -= 1
        return ans + [mi]