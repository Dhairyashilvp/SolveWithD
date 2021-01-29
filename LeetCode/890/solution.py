class Solution:
    def match(self, word, pattern):
        p1 = {}
        p2 = {}
        for i in range(len(word)):
            w ,p = word[i], pattern[i]
            if p not in p1:
                p1[p] = w
            if w not in p2:
                p2[w] = p
            if p1[p] != w or p2[w] != p:
                return False
        return True
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for w in words:
            if self.match(w, pattern):
                ans.append(w)
        return ans
                    
        