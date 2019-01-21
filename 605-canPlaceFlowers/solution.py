class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        counter = 0
        '''

        # greedy solution. check indices nearby O(N), 80%
        flowerbed.insert(0, 0)
        flowerbed.insert(len(flowerbed), 0)
        ind=1

        while ind<len(flowerbed)-1:
            if flowerbed[ind]:
                ind+=2
            else:
                if not(flowerbed[ind-1] or flowerbed[ind+1]):
                    # print(ind)
                    flowerbed[ind]=1
                    counter+=1
                    ind+=2
                else:
                    ind+=1

        return counter>=n
        '''

        # same solution without list-extension O(N), 60%
        ind=0
        while ind<len(flowerbed):
            if flowerbed[ind]==0 and (ind==0 or flowerbed[ind-1]==0) and (ind==len(flowerbed)-1 or flowerbed[ind+1]==0):
                counter+=1
                flowerbed[ind]=1
            if counter>=n:
                return True
            ind+=1

        return False





