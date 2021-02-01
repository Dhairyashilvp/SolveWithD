class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # ans = 0
        # l = len(arr)
        # for i, e in enumerate(arr):
        #     # print("(i + 1):",(i + 1),"(l - i) +1:",((l - i) +1),"2 * e:",2 * e)
        #     # print(((i + 1) * (l - i) +1) / 2 * e)
        #     # ans += ((i + 1) * (l - 1) +1) / 2 * e
        #     ans += ((i + 1) * (l - i) + 1) / 2 * e
        # return ans
        # res, n = 0, len(arr)
        # for i, a in enumerate(arr):
        #     res += ((i + 1) * (n - i) + 1) / 2 * a
        # return res
        res = 0; freq = 0; n = len(arr)
        for i in range(n):
            freq = freq-(i+1)//2+(n-i+1)//2
            res += freq*arr[i]
        return res