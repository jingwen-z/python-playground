# Easy
#
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
#
# Find and return the maximum profit you can achieve.
#
# Constraints:
# - 1 <= prices.length <= 3 * 104
# - 0 <= prices[i] <= 10^4

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if prices == sorted(prices):
            profit = prices[-1] - prices[0]
        elif prices == sorted(prices, reverse=True):
            profit = 0
        else:
            for i, val in enumerate(prices):
                if i + 1 <= len(prices) - 1:
                    if prices[i] >= prices[i + 1]:
                        profit += 0
                    else:
                        profit += prices[i + 1] - prices[i]

        return profit
