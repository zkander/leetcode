#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        arr = [[]]

        for i in range(len(nums)):
            n = len(arr)
            num = nums[i]
            for j in range(0, n):
                t = arr[j].copy()
                t.append(num)
                arr.append(t)

        return arr


# @lc code=end
