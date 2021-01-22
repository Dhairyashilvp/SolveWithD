class Solution:
    def scoreOfParentheses(self, S: str) -> int:
#         ans = [0]
        
#         for c in S:
#             if c == "(":
#                 ans.append(0)
#             else:
#                 A = ans.pop()
#                 ans[-1] += max(A * 2, 1)
#         return ans[0]

        if not S:
            return 0
        
        def score(i, j):
            ans = 0
            lefty = 0
            start = i
            for i in range(i, j):
                lefty += 1 if S[i] == "(" else -1
                if not lefty:
                    if i - start == 1:
                        ans += 1
                    else:
                        ans += 2 * score(start + 1, i)
                    start = i + 1
            return ans
        
        return score(0, len(S))