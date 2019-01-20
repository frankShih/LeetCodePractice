# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not(root):
            return True

        def treeH(root):
            if not(root):
                return 0

            ll = treeH(root.left)
            rr = treeH(root.right)
            return 1+max(ll, rr)

        if abs(treeH(root.right) - treeH(root.left))>1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


        '''
        def height(node):
            if not node:
                return 0
            l,r = height(node.left), height(node.right)
            if l==None or r==None: return
            if abs(l-r)<2:
                return 1+max(l,r)

        # None happens when tree is unbalanced so nothing return
        return height(root)!=None
        '''
