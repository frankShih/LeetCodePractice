class MyStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.que1 = []
        self.que2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.que1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.que1)>1:
            self.que2.append(self.que1.pop(0))
        result = self.que1.pop(0)
        self.que1, self.que2 = self.que2, self.que1
        return result

    def top(self):
        """
        :rtype: int
        """
        return self.que1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.que1
        