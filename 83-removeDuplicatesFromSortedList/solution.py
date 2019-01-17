# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        if not(head) or not(head.next) :
            return head;

        current = head;

        while current.next:
            if current.val==current.next.val:
                current.next =  current.next.next;
            else:
                current =  current.next;
        '''

        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                # skip duplicated node
                cur.next = cur.next.next

            # not duplicate of current node, move to next node
            cur = cur.next

        return head