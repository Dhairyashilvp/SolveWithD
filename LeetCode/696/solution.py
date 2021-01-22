class Solution:
    def countBinarySubstrings(self, s: str) -> int:
#         count = [1]
#         ret = 0
#         for i in range(1, len(s)):
#             if s[i] == s[i-1]:
#                 count[-1] += 1
#             else:
#                 count.append(1)
                
#         for i in range(1,len(count)):
#             ret += min(count[i], count[i-1])
#             print(count[i], " ",count[i-1])
#         return ret
        previous, current, ans = 0 , 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current += 1
            else:
                ans += min(previous , current)
                previous , current = current , 1
        ans += min(previous , current)
        return ans