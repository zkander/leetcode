#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.identicalTrees(root, subRoot):
            return True

        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return l or r

    def identicalTrees(self, a, b):
        # 1. Both empty
        if a is None and b is None:
            return True

        # 2. Both non-empty -> Compare them
        if a is not None and b is not None:
            return ((a.val == b.val) and
                    self.identicalTrees(a.left, b.left) and
                    self.identicalTrees(a.right, b.right))

        # 3. one empty, one not -- false
        return False


# @lc code=end
