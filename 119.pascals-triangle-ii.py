#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        triangle = [[] for _ in range(rowIndex+1)]

        triangle[0].append(1)

        for i in range(1, rowIndex+1):
            triangle[i].append(1)
            
            for j in range(1, len(triangle[i-1])):
                sum = triangle[i-1][j] + triangle[i-1][j-1]
                triangle[i].append(sum)
            triangle[i].append(1)

        return triangle[rowIndex]


# @lc code=end
