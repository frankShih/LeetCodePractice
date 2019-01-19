# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        nodes = set()
        
        while head:
            if head in nodes:
                return head
            else:
                nodes.add(head)
                head=head.next
        '''

        # ***mathmetical prove***
        # Suppose the first meet at step k,the length of the Cycle is r ... 2k-k=nr,k=nr
        # distance between the start node of list and the start node of cycle is s. 
        # distance between the start node of cycle and the first meeting node is m ... s=k-m
        # s=nr-m=(n-1)r+(r-m),here we takes n = 1.
        # so, using one pointer start from the start node of list, another pointer start from the first meeting node
        start = head
        slow, fast = head, head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                while start!=slow:
                    start=start.next
                    slow=slow.next
                return start    
        
        return None        