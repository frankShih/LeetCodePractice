# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n == 0:
            return []
        memo = {}
        helper(1, n+1, memo)
        return memo[(1, n+1)]
        # since top-down have to deal with object-copying,
        # bottom-up to create trees would be more efficient

        def helper(start, end, memo):  # [start,end)
            if (start, end) in memo:
                return memo[(start, end)]
            if start >= end:  # no value
                memo[(start, end)] = [None]
                return [None]
            if start + 1 == end:  # one value
                temp = [TreeNode(start)]
                memo[(start, end)] = temp
                return temp

            ans = []
            for root in range(start, end):
                for left in helper(start, root, memo):
                    for right in helper(root+1, end, memo):
                        newTree = TreeNode(root)
                        newTree.left = left
                        newTree.right = right
                        ans.append(newTree)
            memo[(start, end)] = ans
            return ans
