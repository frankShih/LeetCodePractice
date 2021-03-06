# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        # recursive DFS in-order traversal O(N), memory optimized
        self.count = k

        def helper(root):
            if not root:
                return None

            temp = helper(root.left)
            if temp!=None:
                return temp

            self.count-=1
            if self.count==0:
                return root.val

            temp = helper(root.right)
            if temp!=None:
                return temp

            return None

        return helper(root)
        '''

        # more clean solution, using array to keep smallest values O(N)
        def inorder(root, cand):
            if not root:
                return root
            inorder(root.left, cand)
            # This line is critical to stop early
            if len(cand) == k:
                return

            cand.append(root.val)
            inorder(root.right, cand)

        cand = []
        inorder(root, cand)
        return cand.pop()
        '''
