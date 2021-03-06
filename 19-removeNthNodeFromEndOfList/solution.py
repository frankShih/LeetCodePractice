# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''
        start = ListNode(0)
        start.next, nodelist  = head, [start]
        # using a list to keep only N nodes
        while head.next:
            if len(nodelist) == n:
                nodelist.pop(0)
            nodelist.append(head)
            head = head.next
        nodelist[0].next = nodelist[0].next.next
        return start.next
        '''

        if n<=0 or head==None:  return head
        if n >= self.removeNthFromEndAux(head,n): # will remove head!
            return head.next
        else:
            return head

    def removeNthFromEndAux(self, node, n):
        if node==None:  return 0
        rIdx = self.removeNthFromEndAux(node.next, n)
        if rIdx==n:  # assume n always >= 1, so node.next.next must exist
            node.next = node.next.next
        return 1+rIdx


