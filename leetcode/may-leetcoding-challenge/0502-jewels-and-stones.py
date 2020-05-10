# You're given strings J representing the types of stones that are jewels, and S
# representing the stones you have.  Each character in S is a type of stone you
# have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are
# letters. Letters are case sensitive, so "a" is considered a different type of
# stone from "A".
#
# Example 1:
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
# Example 2:
#
# Input: J = "z", S = "ZZ"
# Output: 0
#
# Note:
#
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

# method 1: Runtime: 20 ms, Memory Usage: 13.7 MB
class Solution1:
    def numJewelsInStones(self, J: str, S: str) -> int:
        out = 0
        stone_dict = {}
        for s in S:
            if not s in stone_dict:
                stone_dict[s] = 1
            else:
                stone_dict[s] += 1

        for j in J:
            if j in stone_dict:
                out += stone_dict[j]

        return out

# method 2: Runtime: 28 ms, Memory Usage: 13.9 MB
class Solution2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        out = 0
        jewel = set(J)

        for s in S:
            if s in jewel:
                out += 1
        return out