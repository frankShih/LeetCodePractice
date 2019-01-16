class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        counter = 0
        temp = x^y

        # fatser way, 99%
        while temp:
            # print(temp)
            temp&=(temp-1)
            counter+=1

        '''
        # naive Solution 90%
        while temp:
            if temp%2:
                counter+=1
            temp = temp//2
        '''

        return counter