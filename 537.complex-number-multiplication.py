#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        sign = False
        real = ""
        nums = []
        for s in num1:
            if ((s == "-" or s == "+") and (real != "-" and real != "+" and real != "")):
                sign == True
                nums.append(real)
                real = s

            if ((s == "-" or s == "+") and (real == "-" or real == "+" or real == "")):
                real = s

            elif (s == "i"):
                nums.append(real)

            elif (s.isnumeric()):
                if (sign):
                    sign = False
                real = real + s
        sign = False
        real = ""
        for s in num2:
            if (((s == "-" or s == "+") and (real != "-" and real != "+" and real != ""))):
                sign == True
                nums.append(real)
                real = s

            if ((s == "-" or s == "+") and (real == "-" or real == "+" or real == "")):
                real = s

            elif (s == "i"):
                nums.append(real)

            elif (s.isnumeric()):
                if (sign):
                    sign = False
                real = real + s
       

        arr = []

        arr.append(int(nums[0]) * int(nums[2]))
        arr.append(int(nums[0]) * int(nums[3]))
        arr.append(int(nums[1]) * int(nums[2]))
        arr.append((int(nums[1]) * int(nums[3])) * -1)

        i = arr[1] + arr[2]
        r = arr[0] + arr[3]

        return str(r) + "+" + str(i) + "i"


# @lc code=end
