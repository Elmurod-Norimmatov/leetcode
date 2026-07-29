# ACCEPTED

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        s = set(ransomNote)

        for i in s:
            if ransomNote.count(i) > magazine.count(i):
                return False

        return True