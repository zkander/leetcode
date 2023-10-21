#
# @lc app=leetcode id=553 lang=python3
#
# [553] Optimal Division
#

# @lc code=start
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:

        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        strNums = list(map(str, nums))
        ans = str(nums[0]) + "/(" + "/".join(strNums[1:])+")"
        return ans

# @lc code=end
