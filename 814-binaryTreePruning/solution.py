# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # DFS solution O(N)
        def helper(node):
            if not node:
                return False
            if helper(node.left):
                node.left=None
            if helper(node.right):
                node.right=None

            if node.val==0 and not(node.left or node.right):
                return True

            return False

        helper(root)

        return root
