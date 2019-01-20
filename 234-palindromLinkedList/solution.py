# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        # using list 45%, time: O(N) space: O(N)
        tempList = []

        while head:
            tempList.append(head.val)
            head = head.next

        length, left, right = len(tempList), -1, -1
        left = length//2-1
        if length%2:
            right = length//2+1
        else:
            right = length//2

        while left>=0 and right<length:
            if tempList[left]!=tempList[right]:
                return False

            left-=1
            right+=1

        return True
        '''

        # reverse linkedList 67%, time: O(N), space: O(1)
        length=0
        curr = head
        while curr:
            curr = curr.next
            length+=1

        if length<2:
            return True

        breakLen = length//2-1
        left = head
        right = left.next

        while breakLen:
            temp = right
            right = right.next
            temp.next = left
            left=temp
            breakLen-=1

        if length%2:
            right = right.next

        while left and right:
            if left.val!=right.val:
                return False

            left = left.next
            right = right.next

        return True