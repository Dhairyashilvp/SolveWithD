class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # d = {}
        # for i in range(len(s)):
        #     d[indices[i]] = s[i]
        ans = ""
        # for i in range(len(s)):
        #     ans += d[i]
        # print(ans)
        # return ans
        # for i in range(len(s)):
        #     ans += s[indices.index(i)]
        # print(ans)
        # return ans
        shuffled_str = [''] * len(s)
        
        for curr_index, final_index in enumerate(indices):
            shuffled_str[final_index] = s[curr_index]
            
        return ''.join(shuffled_str)
    