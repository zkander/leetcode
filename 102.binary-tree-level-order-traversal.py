#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [[root]]
        if root == None:
            return []
        ans = [[root.val]]
        while queue:
            d = queue.pop(0)
            queue.append([])
            ans.append([])
            for i in d:
                if i.right == None and i.left:
                    queue[-1].append(i.left)
                    ans[-1].append(i.left.val)
                    continue

                if i.left == None and i.right:
                    queue[-1].append(i.right)
                    ans[-1].append(i.right.val)
                    continue

                if i.left == None and i.right == None:
                    continue

                queue[-1].append(i.left)
                ans[-1].append(i.left.val)
                queue[-1].append(i.right)
                ans[-1].append(i.right.val)

            if queue[-1] == []:
                del queue[-1]

            if ans[-1] == []:
                del ans[-1]

        return ans

# @lc code=end
