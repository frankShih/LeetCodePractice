class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 99%   built-in function
        '''
        nums.sort(reverse=True)
        return nums[k]
        '''
        self.myQuickSort(nums, 0, len(nums)-1)
        return nums[-k]


    # 3% O(N*log(N)), obtain O(N*log(K)) using heapSort
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