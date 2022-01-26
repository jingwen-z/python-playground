# Easy
#
# Write a function that reverses a string. The input string is given as an array of characters "s".
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
