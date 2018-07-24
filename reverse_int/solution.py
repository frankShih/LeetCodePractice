class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        #70%
        flag = x>0
        result = 0
        x = x if flag else -1*x
        MAX_INT, MIN_INT = 2**31-1, -1*2**31    
        while x>0:
            result = result*10 + x%10
            # print result
            x /=10
            if result>MAX_INT or result<MIN_INT:
                return 0
            
        return result if flag else -1*result     