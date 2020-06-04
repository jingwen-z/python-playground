# Given a m * n matrix of ones and zeros, return how many square submatrices
# have all ones.
#
# Example 1:
#
# Input: matrix =
# [
#     [0,1,1,1],
#     [1,1,1,1],
#     [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
#
# Example 2:
#
# Input: matrix =
# [
#     [1,0,1],
#     [1,1,0],
#     [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.
#
#
#
# Constraints:
#
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        nrows = len(matrix)
        ncols = len(matrix[0])

        output = 0
        for r in range(nrows):
            for c in range(ncols):
                if matrix[r][c] == 0:
                    pass
                elif r == 0 or c == 0:
                    output += 1
                else:
                    min_neighbour = min(matrix[r][c - 1],
                                        matrix[r - 1][c - 1],
                                        matrix[r - 1][c])
                    matrix[r][c] += min_neighbour
                    output += matrix[r][c]

        return output
