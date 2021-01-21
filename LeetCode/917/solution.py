class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        l = 0
        r = len(S) - 1
        st = list(S)
        print(st)
        while l < r:
            while l < r and not st[l].isalpha():
                l += 1
            while l < r and not st[r].isalpha():
                r -= 1
            st[l], st[r] = st[r], st[l]
            l += 1
            r -= 1
        return "".join(st)