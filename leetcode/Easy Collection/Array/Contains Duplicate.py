# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
