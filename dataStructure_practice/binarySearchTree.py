class TreeNode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent TreeNode
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        
        print( self.data),
        
        if self.right:
            self.right.PrintTree()

if __name__ == "__main__":
    # Use the insert method to add TreeNodes
    root = TreeNode(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)

    root.PrintTree()