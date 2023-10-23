#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        i = 1
        mx = 0
        while i < len(prices):
            if (prices[j] > prices[i]):
                j = i
                i += 1
            else:
                mx = max(mx, prices[i] - prices[j])
                i += 1

        return mx


# @lc code=end
