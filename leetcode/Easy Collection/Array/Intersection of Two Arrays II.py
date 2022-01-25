# Easy
#
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
#
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = 0
        n = 0
        l = []

        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)

        while m < len(nums1) and n < len(nums2):
            if sorted_nums1[m] < sorted_nums2[n]:
                m += 1
            elif sorted_nums2[n] < sorted_nums1[m]:
                n += 1
            else:
                l.append(sorted_nums1[m])
                m += 1
                n += 1
        return l
