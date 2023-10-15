#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dic = dict()
        queue = [root]
        while queue:
            r = queue.pop(0)

            if r.left == None and r.right:
                sum = r.right.val + r.val

                if dic.get(sum):
                    dic[sum] += 1
                else:
                    dic[sum] = 1

                queue.append(r.right)
                continue

            if r.right == None and r.left:
                sum = r.left.val + r.val
                if dic.get(sum):
                    dic[sum] += 1
                else:
                    dic[sum] = 1

                queue.append(r.left)
                continue
            
            if r.left == None and r.right == None:
                sum = r.val
                if dic.get(sum):
                    dic[sum] += 1
                else:
                    dic[sum] = 1
                continue

            sum = r.val + r.left.val + r.right.val
            if dic.get(sum):
                dic[sum] += 1
            else:
                dic[sum] = 1

            queue.append(r.left)
            queue.append(r.right)

        sDic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        sDic = dict(sDic)
        mx = list(dic.values())[0]
        ans = []

        for i in (list(dic.keys())):
            if dic[i] == mx:
                ans.append(i)

        return ans


# @lc code=end
