class Solution:
    def compare(self,arr1, arr2): 
        for i in range(256): 
            if arr1[i] != arr2[i]: 
                return False
        return True
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        lenp = len(p)
        lens = len(s)
        if lenp > lens:
            return []
        countp = [0] * 256
        counts = [0] * 256
        
        for i in range(lenp):
            countp[ord(p[i])] += 1
            counts[ord(s[i])] += 1            
        # print(countp)
        # print(counts)
        ans = []
        for i in range(lenp,lens):
            if self.compare(countp,counts):
                ans.append(i-lenp)
            counts[ord(s[i])] += 1
            counts[ord(s[i-lenp])] -= 1
        if self.compare(countp,counts):
            ans.append(lens-lenp)
        return ans
            