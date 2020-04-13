# Easy
#
# Given a m * n matrix of distinct numbers, return all lucky numbers in the
# matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element
# in its row and maximum in its column.
#
#
# Example 1:
#
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row
# and the maximum in its column
#
# Example 2:
#
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row
# and the maximum in its column.
#
# Example 3:
#
# Input: matrix = [[7,8],[1,2]]
# Output: [7]
#
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 10^5.
# All elements in the matrix are distinct.

import numpy as np

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        out=[]

        for l in matrix:
            c_min_idx = np.argmin(l)
            c_min_val = l[c_min_idx]

            col_values = []
            for i in range(r):
                col_values.append(matrix[i][c_min_idx])
            if c_min_val == max(col_values):
                out.append(c_min_val)
            else:
                pass

        return out