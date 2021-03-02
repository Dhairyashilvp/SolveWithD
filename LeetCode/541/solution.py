# class Solution(object):
#     def reverseStr(self, s, k):
#         ans = list(s)
#         for i in range(0, len(ans), 2*k):
#             ans[i:i+k] = reversed(ans[i:i+k])
#         return "".join(ans)
    
    
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        i = 0
        while i < len(s):
            if i+2*k < len(s):
                res += s[i:i+k][::-1]
                res += s[i+k:i+2*k]
            elif i+2*k >= len(s) and i+k < len(s):
                res += s[i:i+k][::-1]
                res += s[i+k:]
            elif i+k >= len(s):
                res += s[i:][::-1]
            i += 2*k
        return res