# Easy
#
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, (2^31) - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x_pos = (-1) * x
        else:
            x_pos = x

        reversed_nb = 0
        while x_pos > 0:
            rest = x_pos % 10
            reversed_nb = reversed_nb * 10 + rest
            x_pos = x_pos // 10

        if x < 0:
            if (-1) * reversed_nb < (-2) ** 31 \
                    or (-1) * reversed_nb > (2 ** 31) - 1:
                return 0
            else:
                return (-1) * reversed_nb
        else:
            if (-1) * reversed_nb < (-2) ** 31 \
                    or (-1) * reversed_nb > (2 ** 31) - 1:
                return 0
            else:
                return reversed_nb
