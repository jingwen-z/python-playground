# Easy
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            t_list = []
            t_list[0:] = t

            not_in_nb = 0
            for c in s:
                if c not in t_list:
                    not_in_nb += 1
                    return False
                else:
                    t_list.remove(c)
            if not_in_nb == 0:
                return True
