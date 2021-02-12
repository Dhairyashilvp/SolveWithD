class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p= 0, 1
        for i in str(n):
            num = int(i)
            print(num)
            p *= num
            s += num
        return p - s
        # while n != 0:
        #     num = (n % 10)
        #     p = p * num
        #     n = n // 10
        #     s += num
        # return p - s