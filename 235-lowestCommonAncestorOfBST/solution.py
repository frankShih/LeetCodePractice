# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        '''
        # DFS, recursive checking value with BST features O(log(N))

        if (root.val-p.val)*(root.val-q.val)<=0:
            return root
        elif (root.val > p.val ):   # root is larger than both values
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        '''


        # DFS, iterative checking value with BST features O(log(N))
        p_val = p.val
        q_val = q.val
        node = root

        while node:
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # p_val < parent_val < q_val / p_val > parent_val > q_val
                return node