# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """

        if not root:
            return TreeNode(v)

        # BFS solution O(N), 65%
        dummyNode = TreeNode(None)
        dummyNode.left = root

        treeQ = [(dummyNode, 0)]

        while treeQ:
            node, level = treeQ.pop(0)
            if not node:
                continue
            # print(node.val, level)
            if level==d-1:
                left, right = node.left, node.right
                node.left, node.right = TreeNode(v), TreeNode(v)
                node.left.left, node.right.right = left, right
            else:
                treeQ.append((node.left, level+1))
                treeQ.append((node.right, level+1))

        return dummyNode.left