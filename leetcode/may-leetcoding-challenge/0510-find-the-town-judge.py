# In a town, there are N people labelled from 1 to N.  There is a rumor that one
# of these people is secretly the town judge.
#
# If the town judge exists, then:
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
#
# You are given trust, an array of pairs trust[i] = [a, b] representing that the
# person labelled a trusts the person labelled b.
#
# If the town judge exists and can be identified, return the label of the town
# judge.  Otherwise, return -1.
#
#
# Example 1:
#
# Input: N = 2, trust = [[1,2]]
# Output: 2
#
# Example 2:
#
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
#
# Example 3:
#
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
#
# Example 4:
#
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
#
# Example 5:
#
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
#
#
# Note:
#
# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N

class Solution1:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        not_judge = set([lst[0] for lst in trust])
        candidates_dict = {i: 0 for i in range(1, N + 1)}

        for lst in trust:
            candidates_dict[lst[1]] += 1

        candidate_exist = 0
        for candidate, times in candidates_dict.items():
            if times == N - 1 and not candidate in not_judge:
                candidate_exist += 1
                return candidate

        if candidate_exist == 0:
            return -1


class Solution2:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        candidates = [0] * N
        for lst in trust:
            candidates[lst[0] - 1] -= 1
            candidates[lst[1] - 1] += 1
        if N - 1 in candidates:
            return candidates.index(N - 1) + 1
        else:
            return -1
