#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = dict([])
        for i in range(len(strs)):
            t = ''.join(sorted(strs[i]))
            dic[t] = []
        for i in range(len(strs)):
            t = ''.join(sorted(strs[i]))
            dic[t].append(strs[i])
        return dic.values()


# @lc code=end
