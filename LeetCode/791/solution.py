class Solution:
    def customSortString(self, S: str, T: str) -> str:
        # w1 = list(S)
        # ans = []
        # rest = ""
        # for c in T:
        #     if c in w1:
        #         if T.index(c) >= w1.index(c):
        #             ans.insert(w1.index(c),c)
        #         else:
        #             ans.append(c)
        #     else:
        #         rest += c
        #     print(ans, " " , rest)
        ans, cnt = [], collections.Counter(T)
        for c in S:
            if cnt[c]: ans.extend(c * cnt.pop(c))
        for c, v in cnt.items():
            ans.extend(c * v)
        return ''.join(ans);
        