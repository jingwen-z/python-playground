# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Output: true
#
# Example 2:
#
# Input: 14
# Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, s = 1, 1

        while s < num:
            i += 2
            s += i

        return s == num
