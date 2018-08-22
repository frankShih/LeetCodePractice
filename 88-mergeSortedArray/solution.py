class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        '''
        # 99%
        index1, index2 = m-1, n-1
        
        for i in range(len(nums1)-1, -1, -1):
            #print [index1, index2]
            
            if index2 < 0 or (nums1[index1] > nums2[index2] and index1>-1) :
                #list2 is empty or list1 have bigger value remained
                nums1[i] = nums1[index1];
                index1-=1;
            
            else:
                nums1[i] = nums2[index2];
                index2-=1;        
        
        '''

        # 35%                    
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]    
        
            
            