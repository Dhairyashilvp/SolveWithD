class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans = 4 
        num = 12
        if N < 11:
            ans = 0
            num = 1
        for d in range(num, N+1):
            ds = str(d)
            if "3" in ds or "4" in ds or "7" in ds:
                pass
            elif "2" in ds or "5" in ds or "6" in ds or "9" in ds:
                    ans += 1
        return ans