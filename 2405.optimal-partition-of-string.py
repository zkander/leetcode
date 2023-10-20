#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        n = set()

        for i in s:
            if i in n:
                count += 1
                n.clear()
            n.add(i)
        return count


# @lc code=end
