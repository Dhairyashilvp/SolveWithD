class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.setdefault(c,0) + 1
        print(d)
        totalpairs, odd = 0, 0
        for c in d:
            count = d[c]
            pair = count // 2
            print(pair)
            if not odd  and count - pair * 2 > 0:
                odd = 1
            totalpairs += pair
        return totalpairs * 2 + odd