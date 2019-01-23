# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        # recursively find index & split into left/right part O(N)
        def helper(preorder, postorder):
            if not(preorder or postorder):
                return

            split_idx = -1
            root = TreeNode(preorder[0])

            for i, v in enumerate(postorder):
                if split_idx == i:
                    # postLeft = postorder[:i]
                    # postRight = postorder[i:-1]
                    # preLeft = preorder[1:split_idx+1]
                    # preRight = preorder[split_idx+1:]
                    root.left = helper(preorder[1:split_idx+1], postorder[:i])
                    root.right = helper(preorder[split_idx+1:], postorder[i:-1])
                    break

                curInd = preorder.index(postorder[i])
                split_idx = curInd if curInd>split_idx else split_idx

            return root


        return helper(pre, post)

