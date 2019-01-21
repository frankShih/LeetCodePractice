class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        counter=0
        if not points:
            return counter

        length = len(input)
        '''
        # greedy, sort & check startInd O(N^log(N)), 83%
        input=sorted(points ,key=lambda l:l[0], reverse=True)
        previous_start=float('inf')

        for i in range(0, length):
            if previous_start>input[i][1]:
                previous_start=input[i][0]
                counter+=1

        return counter
        '''

        # greedy, check endInd O(N^log(N)), 70%
        points=sorted(points ,key=lambda l:l[1])
        previous_end=float('-inf')

        for point in points:
            if previous_end<point[i][0]:
                previous_end=point[i][1]
                counter+=1

        return counter
