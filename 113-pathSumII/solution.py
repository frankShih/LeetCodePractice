# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, summ):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        result=[]
        
        if not root:
            return result

        # BFS, 28%
        taskQ = [[root, []]]    

        while taskQ:
            curr, path = taskQ.pop(0)
            
            if not curr:
                continue
            # print(curr.val, path)
            if sum(path)==summ-curr.val and not(curr.left) and not(curr.right):
                result.append(path+[curr.val])
                continue
            
            taskQ.append([curr.left, path+[curr.val]])
            taskQ.append([curr.right, path+[curr.val]])

        return result