#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in range(len(operations)):
            ch = operations[i]

            if (ch == "C"):
                arr.pop()
            elif (ch == "D"):
                arr.append(int(arr[-1])*2)
            elif (ch == "+"):
                arr.append(int(arr[-1]) + int(arr[-2]))
            else:
                arr.append(int(operations[i]))
            print(arr)

        return sum(arr)


# @lc code=ends
