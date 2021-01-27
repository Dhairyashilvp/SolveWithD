class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        elif not ransomNote:
            return True
        for c in set(ransomNote):
            if c not in magazine or ransomNote.count(c) > magazine.count(c):
                return False
        return True