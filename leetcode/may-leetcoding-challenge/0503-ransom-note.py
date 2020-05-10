# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == magazine:
            return True
        else:
            for r in ransomNote:
                if r in magazine:
                    magazine = magazine.replace(r, '', 1)
                else:
                    return False
            return True


class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazines_dict = {}
        for m in magazine:
            if m in magazines_dict:
                magazines_dict[m] += 1
            else:
                magazines_dict[m] = 1

        for r in ransomNote:
            if r in magazines_dict and magazines_dict[r] > 0:
                magazines_dict[r] -= 1
            else:
                return False
        return True
