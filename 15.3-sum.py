#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        j = 0 
        k = len(nums)-1
        nums.sort()
        sum = 0
        

        for i in range (len(nums)):
             j = i + 1
             k = len(nums) - 1
             while (j < k):
                sum = int(nums[i]) + int(nums[j]) + int(nums[k])
                if (sum == 0):
                    ans.append([nums[j],nums[i],nums[k]])
                    k-=1
                    j+=1
                    continue 
                if sum < 0: 
                    j+=1
                if sum > 0:
                    k-=1
               
        
        ans = list(map(list, set(map(tuple, ans))))


        return ans
        
# @lc code=end

