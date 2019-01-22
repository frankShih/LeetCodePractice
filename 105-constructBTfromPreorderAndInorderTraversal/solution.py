# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # DFS Solution O(N*log(N))
        if not preorder:
            return None

        # get index of root
        root_idx = inorder.index(preorder[0])
        # split in-order/pre-order list to left/right subtree
        in_left = inorder[:root_idx]
        in_right = inorder[root_idx + 1 :]
        splitLen = 1 + len(in_left)
        pre_left = preorder[1:splitLen]
        pre_right = preorder[splitLen:]

        # recursively create subtrees
        root = TreeNode(inorder[root_idx])
        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        return root
