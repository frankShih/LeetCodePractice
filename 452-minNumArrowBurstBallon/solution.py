class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # 70%
        input=sorted(points ,key=lambda l:l[0], reverse=True)
        length = len(input)        
        counter=0                
        # pre = None
        previous_start=float('inf')
        
        for i in range(0, length):            
            if previous_start>input[i][1]:
                previous_start=input[i][0]
                counter+=1
            else:                
                # pre = input[i]
                # previous_end=pre.end                
                continue                
                # print(pre.start, pre.end)    
            
        return counter
        