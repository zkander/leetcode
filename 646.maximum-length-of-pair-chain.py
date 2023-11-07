#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        count = 0
        i = 1
        n = 0

        arr = []
        for i in range(len(pairs)):

            arr.append(pairs[i][1])

        arr.sort()
        print(arr)

        while (i < len(arr)):
            print(arr[i] > arr[n])
            if arr[i] > arr[n]:
                count += 1
                n = i

            i += 1

        return count + 1


# @lc code=end
