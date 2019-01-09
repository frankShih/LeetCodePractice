class RLEIterator:
    '''
    # memory limit solution
    def __init__(self, A):
        """
        :type A: List[int]
        """
        # print(A)
        self.arr = []
        self.index = 0
        for i in range(0, len(A), 2):
            times, val = A[i], A[i+1]
            for j in range(times):
                self.arr.append(val)
        # print(self.arr)


    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.index+=n
        if self.index<len(self.arr):
            return self.arr[self.index-1]
        else:
            return -1    
    
    '''
        
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.index = 0
        # self.arr = A
        self.length = len(A)//2
        self.summ = [0]*(self.length)
        self.values = [0]*(self.length)
        
        temp = 0
        for i in range(0, self.length):
            times = A[i*2]
            temp+=times
            self.summ[i] = temp
            self.values[i] = A[i*2+1]
            # self.values.append(val)
        
    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.index+=n
        if self.index> self.summ[-1]:
            return -1    
            
        for i in range(self.length):
            if self.summ[i]>=self.index:
                return self.values[i]
        
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)