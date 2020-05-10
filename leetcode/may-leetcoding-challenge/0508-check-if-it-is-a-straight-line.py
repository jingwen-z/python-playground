# You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
# represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.
#
# Example 1:
#
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
#
# Example 2:
#
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
#
# Constraints:
#
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ((first_x, first_y), (second_x, second_y)) = coordinates[:2]

        delta_2x = second_x - first_x
        delta_2y = second_y - first_y

        if delta_2x == 0:
            for coordinate in coordinates[2:]:
                if coordinate[0] != first_x:
                    return False
        else:
            slope = delta_2y / delta_2x
            for coordinate in coordinates[2:]:
                if coordinate[0] == first_x:
                    return False
                else:
                    new_slope = (coordinate[1] - first_y) / (
                        coordinate[0] - first_x)
                    if new_slope != slope:
                        return False
                    else:
                        return True


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ((first_x, first_y), (second_x, second_y)) = coordinates[:2]

        for coordinate in coordinates[2:]:
            return (second_y - first_y) * (coordinate[0] - first_x) == \
                   (coordinate[1] - first_y) * (second_x - first_x)
