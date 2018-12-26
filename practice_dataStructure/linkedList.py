class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

def reverse(self,head):
        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre    
        
if __name__ == "__main__":
    values=[1, 4, 2, 8, 5, 7]

    root = ListNode(values[0])
    curr=root
    for i in range(1, len(values)):
        temp = ListNode(values[i])
        curr.next = temp
        curr = curr.next

    while root:
        print(root.val)
        root = root.next
