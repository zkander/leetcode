#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        c = 0

        for i in range(1, n + 1):
            if n % i == 0:
                c += 1
            if c == k:
                return i

        return -1


# @lc code=end
