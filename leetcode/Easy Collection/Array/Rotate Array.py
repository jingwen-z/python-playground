# Easy
# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        l = []

        if k // len_nums == 0:
            simple_k = k
        else:
            simple_k = k % len_nums

        if simple_k == len_nums:
            l = nums
        else:
            l = nums[-simple_k:] + nums[:(len_nums - simple_k)]

        for i in range(len_nums):
            nums[i] = l[i]
