# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # naive solution O(N+M) 55%
        val1, val2 = 0, 0

        while l1:
            val1*=10
            val1+=l1.val
            l1 = l1.next

        while l2:
            val2*=10
            val2+=l2.val
            l2 = l2.next

        sumUp = str(val1+val2)
        head = ListNode(-1)
        curr = head
        for char in sumUp:
            curr.next = ListNode(int(char))
            curr = curr.next

        return head.next
