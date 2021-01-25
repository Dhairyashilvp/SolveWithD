class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        ans = []
        for c in s:
            if not ans:
                ans.append(c)
            elif (ans[-1].isupper() and ans[-1].lower() == c) or (ans[-1].islower() and ans[-1].upper() == c):
                ans.pop()
            else:
                ans.append(c)
        return "".join(ans)
#         result = []
#         for c in s:
#             if not result:
#                 result.append(c)
#             elif result[-1].isupper() and result[-1].lower() == c:
#                 result.pop()
#             elif result[-1].islower() and result[-1].upper() == c:
#                 result.pop()
#             else:
#                 result.append(c)
#         return ''.join(result)
        
            
            