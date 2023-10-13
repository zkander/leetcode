#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum = 0

        def traverse(node):
            nonlocal sum
            if not node:
                return

            traverse(node.right)
            node.val += sum
            sum = node.val
            traverse(node.left)

        traverse(root)
        return root

# @lc code=end
