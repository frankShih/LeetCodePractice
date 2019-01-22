# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # recursive trimming nodes O(N)
        if not root:
            return root

        # possible situations:
        # 1. current node out of range larger/lesser -> replace it
        # 2. keep checking its descendants
        if root.val<L:
            root = self.trimBST(root.right, L, R)
        elif root.val>R:
            root = self.trimBST(root.left, L, R)
        else:
            root.right = self.trimBST(root.right, L, R)
            root.left = self.trimBST(root.left, L, R)

        return root