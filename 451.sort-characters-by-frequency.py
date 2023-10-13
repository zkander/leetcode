#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = 0
        for i in s:
            dic[i] += 1
        sDict = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        sDict = dict(sDict)
        ans = ""
        for key in sDict:
            ans = ans + (key * sDict[key])
        return ans
# @lc code=end
