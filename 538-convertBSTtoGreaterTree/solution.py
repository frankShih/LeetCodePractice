# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        total = 0
        '''
        # recursive DFS in-order traversal O(N)
        def helper(root, sumup):
            if root:
                # find larger value
                sumup = helper(root.right, sumup)
                # accumulate & modify it
                sumup += root.val
                root.val = sumup
                # then the lesser
                sumup = helper(root.left, sumup)
            return sumup

        helper(root, total)
        return root
        '''

        # iterative DFS in-order traversal, using stack O(N)
        node = root
        stack = []
        while stack or node:
            # push all right-nodes to (root included) the stack.
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val   # accumulate & replace
            node.val = total

            # then left subtree
            node = node.left

        return root