class Solution:
    def maxScore(self, s: str) -> int:
        # if "1" not in s or "0" not in s:
        #     return len(s) - 1
        # maxi = 0
        # for i in range(len(s)-1):
        #     left = s[:i+1]
        #     right = s[i+1:]
        #     if "1" not in left and "0" not in right:
        #         return len(left) + len(right)
        #     else:
        #         maxi = max(maxi, left.count("0") + right.count("1"))
        # return maxi
        # maxi = []
        # for i in range(len(s)-1):
        #     left = s[:i+1]
        #     right = s[i+1:]
        #     if "1" not in left and "0" not in right:
        #         return len(left) + len(right)
        #     else:
        #         maxi.append(left.count("0") + right.count("1"))
        # return max(maxi)
        zeros = 1 if s[0] == '0' else 0
        ones = s.count('1', 1)  # count 1s in s[1:]
        score = zeros + ones
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            score = max(zeros + ones,  score)
        return score