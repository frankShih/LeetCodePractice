# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l, r = 0, n

        while l<=r:
            m = l+(r-l)//2
            # print(l, m, r)
            ans = guess(m)
            if ans == 0:
                return m
            elif ans==1:
                l = m+1
            else:    
                r = m-1

        return 0    