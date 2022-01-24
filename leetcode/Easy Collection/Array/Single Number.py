# Easy
#
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            sorted_nums = sorted(nums)
            s = 0
            for i, val in enumerate(sorted_nums):
                if i % 2 == 0:
                    s += val
                elif i % 2 == 1:
                    s -= val
            return s
