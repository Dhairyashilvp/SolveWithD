class Solution:
    def thousandSeparator(self, n: int) -> str:
#         if n < 1000:
#             return str(n)
#         else:
#             o = str(n % 1000).zfill(3)
#             m = int(n / 1000)
#             return self.thousandSeparator(m) + "." + o
        final = ''
        count = 0
        if n > 999:
            for i in str(n)[::-1]:
                count += 1
                if count == 3:
                    final += str(i)
                    final += '.'
                    count = 0
                else:
                    final += str(i)
            if len(str(n)) % 3 == 0:
                return final[::-1][1:]
            else:
                return final[::-1]
        else:
            return str(n) 