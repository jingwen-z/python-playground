# Easy
#
# Given an array arr, replace every element in that array with the greatest
# element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.
#
#
#
# Example 1:
#
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#
#
#
# Constraints:
#
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output_list = [-1]
        max_val = -1
        for v in arr[::-1]:
            if v > max_val:
                max_val = v
                output_list.append(max_val)
            else:
                output_list.append(max_val)
        output_list = output_list[:-1]

        return output_list[::-1]
