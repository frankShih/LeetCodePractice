# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        result = []
        if not root:
            return result

        '''
        self.undirectGraph = dict()
        # DFS build graph O(N)
        def buildGraph(node):
            self.undirectGraph.setdefault(node.val, [])

            if node.left:
                self.undirectGraph[node.val].append(node.left.val)
                self.undirectGraph.setdefault(node.left.val, [])
                self.undirectGraph[node.left.val].append(node.val)
                buildGraph(node.left)

            if node.right:
                self.undirectGraph[node.val].append(node.right.val)
                self.undirectGraph.setdefault(node.right.val, [])
                self.undirectGraph[node.right.val].append(node.val)
                buildGraph(node.right)

        buildGraph(root)

        # BFS search graph O(N)
        taskQ = [(target.val, 0, None)]
        while taskQ:
            curr, dist, pre = taskQ.pop(0)
            # print(curr, dist, pre)
            if dist==K:
                result.append(curr)
                continue

            for v in self.undirectGraph[curr]:
                if v != pre:
                    taskQ.append((v, dist+1, curr))

        return result
        '''

        # another version, add parent to mimic undirected graph
        def dfs(root, p):
            if not root: return
            root.parent = p
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)
        queue = [target]
        visited = set()
        visited.add(target)

        for i in range(K):
            for i in range(len(queue)):
                curr = queue.pop(0)
                for node in [curr.left, curr.right, curr.parent]:
                    if node and node not in visited:
                        queue.append(node)
                        visited.add(node)
        return [node.val for node in queue]
