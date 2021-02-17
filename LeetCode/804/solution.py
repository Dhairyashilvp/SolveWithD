import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        op = []
        for w in words:
            mc = ""
            for c in w:
                mc += code[ord(c)-ord("a")]
            if mc not in op:
                op.append(mc)
        return len(op)