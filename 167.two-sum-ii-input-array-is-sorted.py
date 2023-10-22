#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        j = 0
        k = len(numbers) - 1

        while j < k:
            total = numbers[j] + numbers[k]
            if total == target:
                ans = [j+1, k+1]
                break
            elif total > target:
                k -= 1
            elif total < target:
                j += 1

        return ans


# @lc code=end
