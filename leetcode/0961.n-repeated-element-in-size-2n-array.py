# Easy
#
# In a array A of size 2N, there are N+1 unique elements, and exactly one of
# these elements is repeated N times.
#
# Return the element repeated N times.
#
# Example 1:
#
# Input: [1,2,3,3]
# Output: 3
#
# Example 2:
#
# Input: [2,1,2,5,3,2]
# Output: 2
#
# Example 3:
#
# Input: [5,1,5,2,5,3,5,4]
# Output: 5
#
# Note:
#
# 4 <= A.length <= 10000
# 0 <= A[i] < 10000
# A.length is even

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        element_count = dict()
        for k in A:
            if not k in element_count:
                element_count[k] = 1
            else:
                element_count[k] += 1
                if element_count[k] == len(A) // 2:
                    return k
