# Easy
#
# Students are asked to stand in non-decreasing order of heights for an annual
# photo.
#
# Return the minimum number of students that must move in order for all students
# to be standing in non-decreasing order of height.
#
# Example 1:
#
# Input: heights = [1,1,4,2,1,3]
# Output: 3
#
# Constraints:
#
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nb_change=0
        sorted_heights = heights.copy()
        sorted_heights.sort()
        for i, v in enumerate(heights):
            if v != sorted_heights[i]:
                nb_change += 1
            else:
                pass
        return nb_change
