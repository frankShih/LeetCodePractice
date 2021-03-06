# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if not head:
            return None

        # build tree with recursion, 55%
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        length = len(nums)


        def buildTree(arr, start, end):
            if start==end: return
            mid = start+(end-start)//2
            # print(start, mid, end)
            root = TreeNode(arr[mid])

            root.left = buildTree(arr, start, mid)
            root.right = buildTree(arr, mid+1, end)

            return root

        return buildTree(nums, 0, length)