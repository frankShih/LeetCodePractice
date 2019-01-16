class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if not num:
            return False

        # naive solution 60%
        l, r = 1, num
        while l<=r:
            m = l+(r-l)//2
            # print(m)
            temp = num/m
            if temp==m:
                return True

            if temp**2>num:
                l=m+1
            else:
                r = m-1

        return False