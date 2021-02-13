class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # arr = [start] * n
        # ans = start
        # for i in range(1, n):
        #     # arr[i] = start + (2 * i)
        #     ans ^= start + (2 * i)
        # print(ans)
        # return ans
        result = 0
        for i in range(start, start+2*n, 2):
            print(i)
            result ^= i
        return result