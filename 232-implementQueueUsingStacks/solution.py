class MyQueue(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        #self.stack1.insert(0, x);
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        # if len(self.stack1)==0: return;
        #del self.stack1[-1];
        if not(self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        #if len(self.stack1)==0: None;
        # return self.stack1[-1];
        if not(self.stack2):
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # return len(self.stack1)==0;
        return not(self.stack1 or self.stack2)
