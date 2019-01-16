# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # naive solution O(M+N), 70%
        head = ListNode(-1)
        curr = head
        while l1 or l2:
            if l1 and l2:
                if l1.val<l2.val:
                    curr.next = l1
                    curr = curr.next
                    l1 = l1.next
                else:
                    curr.next = l2
                    curr = curr.next
                    l2 = l2.next
            elif l1:
                curr.next = l1
                break
            else:   # l2
                curr.next = l2
                break

        return head.next