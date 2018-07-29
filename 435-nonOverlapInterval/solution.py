# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        '''
        # 1%
        if not(intervals): return 0
        input = []
        # for i in intervals:            
        #     input.append([i.start, i.end])
        input=sorted(intervals ,key=lambda l:l.end, reverse=False)
                
        ind, counter=0, 0
        previous_end=-float('inf')
        
        while ind<len(input):
            temp = input[ind]
            for i in range(ind, len(input)):            
                if input[i].end==temp.end:
                    ind+=1    
                    if input[i].start>temp.start:
                       temp = input[i]
                else:
                    break
            
            conflict= previous_end>temp.start
            
            if not(conflict): 
                counter+=1
                previous_end = temp.end
            
        return len(intervals) - counter
 
    
        # 18%        
        if len(intervals)<2: return 0
        input = []
        input=sorted(intervals ,key=lambda l:l.end, reverse=False)
                
        counter=0                
        pre = None
        previous_end=-float('inf')
        
        for i in range(0, len(input)):            
            if previous_end>input[i].start:
                continue
            else:                
                pre = input[i]
                previous_end=pre.end
                counter+=1
                print(pre.start, pre.end)    
            
        return len(intervals) - counter
        '''

        '''
        # 70%
        input=sorted(intervals ,key=lambda l:l.end, reverse=False)
        length = len(input)        
        counter=0                
        # pre = None
        previous_end=-float('inf')
        
        for i in range(0, length):            
            if previous_end<=input[i].start:
                previous_end=input[i].end
            else:                
                # pre = input[i]
                # previous_end=pre.end                
                counter+=1
                # print(pre.start, pre.end)    
            
        return counter
        '''
        
        # 100%
        input=sorted(intervals ,key=lambda l:l.start, reverse=True)
        length = len(input)        
        counter=0                
        # pre = None
        previous_start=float('inf')
        
        for i in range(0, length):            
            if previous_start>=input[i].end:
                previous_start=input[i].start
            else:                
                # pre = input[i]
                # previous_end=pre.end                
                counter+=1
                # print(pre.start, pre.end)    
            
        return counter
 

'''
 [[1, 2], [-1, 2], [1, 12], [10, 12], [-1, 22], [1, 20]]
 [[1,2],[1,2],[1,2]]
 [[1,2],[2, 3],[3,5]]
'''