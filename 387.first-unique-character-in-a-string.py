#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:

        charDict = dict()

        for i in s:
            if (charDict.get(i)):
                charDict[i] += 1
            else:
                charDict[i] = 1

        for i in range(len(list(s))):
            if charDict[s[i]] == 1:
                return i

        return -1

# @lc code=end
