# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        '''
        # using set 70%
        records = set()
        while headA:
            records.add(headA)
            headA = headA.next

        while headB:
            if headB in records:
                return headB

            records.add(headB)
            headB = headB.next

        return None
        '''

        # brilliant rule, 35%
        # Let headA = A + O, headB = B + O, where O is repeated part.
        # To get to O from headA, the length is A + O + B,
        # to get to O from headB, the length is B + O + A
        # meet at minCommonMultiple(A, B) step
        currA, currB = headA, headB

        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA

        return currB
