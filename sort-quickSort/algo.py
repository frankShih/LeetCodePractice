def myQuickSort(self, array, left, right):
        if left>=right: return
        pivot=array[left]
        i, j = left+1, right               
                
        while True:
            while i<=right:
                if pivot<array[i]:
                    break    
                i+=1                                
            while j>left:
                if pivot>array[j]:
                    break
                j-=1
                
            if i>=j: break
            self.swap(array, i, j)
        self.swap(array, left, j)    
        self.myQuickSort(array, left, j-1)
        self.myQuickSort(array, j+1, right)        
        
    def swap(self, array, a, b):        
        array[a], array[b] = array[b], array[a]        