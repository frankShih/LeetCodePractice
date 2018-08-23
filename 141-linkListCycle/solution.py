# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # 24%
        if not(head) or not(head.next): return False
        
        fast, slow = head, head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True
        return False
        
        # 60%
        nodes = set()
        while head:
            if head in nodes:
                return True
            else:
                nodes.add(head)
                head=head.next
                
        return False        

