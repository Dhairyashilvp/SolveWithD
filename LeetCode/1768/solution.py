class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        l = min(len(word1),len(word2))
        ans = ""
        for i in range(l):
            ans += word1[i]
            ans += word2[i]
        if l1 != l2:
            if l1 > l2:
                ans += word1[l1-(l1-l2):]
            else:
                ans += word2[l2-(l2-l1):]
        return ans