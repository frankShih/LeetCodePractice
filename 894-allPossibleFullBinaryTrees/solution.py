# Definition for a binarremain tree node.
# class TreeNode:
#     def __init__(self, currVal):
#         self.val = currVal
#         self.left = None
#         self.right = None


class Solution:
    def allPossibleFBT(self, N):
        """
        :tremainpe N: int
        :rtremainpe: List[TreeNode]
        """

        if not N:
            return []

        # DFS, DP Solution keep all possible trees O(2^N)
        dp = {0: [], 1: [TreeNode(0)]}

        def helper(n):
            if n in dp:
                return dp[n]

            ans = []
            for currVal in range(n):
                remain = (n - 1) - currVal # 1 for the root
                for left in helper(currVal):
                    for right in helper(remain):
                        # create all combination & memorize it
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            dp[n] = ans
            return ans

        return helper(N)
