# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None;
        if not head.next:
            return head;

        pre, cur = head, head.next;
        pre.next = None;
        '''
        #iterative

        #print cur.val
        while cur!=None:
            temp = cur.next
            cur.next = pre;
            pre = cur;
            cur = temp;

        return pre;

        '''

        #recursive
        return self.rev(pre, cur);



    def rev(self, re, node):
        temp = node.next;
        node.next = re;
        if temp==None:
            return node;
        return self.rev(node, temp);


