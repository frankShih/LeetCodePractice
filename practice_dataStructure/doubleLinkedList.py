class ListNode:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

if __name__ == "__main__":
    values=[1, 4, 2, 8, 5, 7]

    root = ListNode(values[0])
    pre, curr = None, root
    for i in range(1, len(values)):
        temp = ListNode(values[i])
        curr.prev = pre
        curr.next = temp
        pre = curr
        curr = curr.next

    while root:
        if root.prev:
            print(root.prev.data)
        print(root.data)
        if root.next:
            print(root.next.data)
        print("--------------------")
        root = root.next

    # insert at begining
    NewNode = ListNode(123)
    NewNode.next = root
    if root:
        root.prev = NewNode
    root = NewNode
    
      