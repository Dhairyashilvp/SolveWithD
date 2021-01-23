class Solution:
    def reformat(self, s: str) -> str:
        if len(s) > 1 and (s.isnumeric() or s.isalpha()):
            return "" 
        n, a = [], []
        for i in range(len(s)):
            if s[i].isdigit():
                n.append(s[i])
            else:
                a.append(s[i])
        l = len(a) - len(n)
        ret = ""
        if l == 1:
            while n:
                ret += a.pop()
                ret += n.pop()
            ret += a.pop()
        elif l == 0:
            while a:
                ret += a.pop()
                ret += n.pop()
        elif l == -1:
            while a:
                ret += n.pop()
                ret += a.pop()
            ret += n.pop()
        else:
            return ""
        return ret
        