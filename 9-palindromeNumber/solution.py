class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        # string fashion O(N), 59%
        temp = str(x)
        length = len(temp)
        for i in range(0, length/2):
            #print len(temp)/2
            if temp[i]!=temp[length-i-1]:
                return False
                
        return True
        '''
        
        # pure math fashion, 66%
        if x == 0: 
            return True
        if x < 0 or x%10 == 0: 
            return False

        invt_x = 0
        while x > invt_x:
            invt_x = invt_x*10 + x%10
            x //= 10

        # even/odd number of digits
        return x == invt_x or x == invt_x//10