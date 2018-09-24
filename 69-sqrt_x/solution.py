class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 100%
        '''
        return int(x**0.5)
        '''
        
        # 45%   binary search
        l, h = 1, x
        
        while l<=h:
            m = l+ (h-l)//2
            sqrt=x/m
            if sqrt==m:
                # print(1)
                return m            
            elif sqrt>m:
                # print(2)
                l=m+1
            else:
                # print(3)
                h=m-1
                
        return int(h)