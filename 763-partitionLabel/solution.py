class Solution(object):
    def init_list_of_objects(self, size):
        list_of_objects = list()
        for i in range(0,size):
            list_of_objects.append( list() ) #different object reference each time
        return list_of_objects

    
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        # 72%     
        counter = self.init_list_of_objects(26)
        intervals = []

        for i in range(len(S)):
            counter[ord(S[i])-97].append(i)

        for c in counter:
            if not(c):
                continue
            elif len(c)==1:
                intervals.append([c[0], c[0]])
            else:
                intervals.append([c[0], c[len(c)-1]])        

        if not(intervals): return [0]
        
        intervals=sorted(intervals ,key=lambda l:l[0], reverse=False)        
        
        result = []
        previous_end=intervals[0][1]
        previous_start=intervals[0][0]

        for i in range(1, len(intervals)):            
            if previous_end<intervals[i][1]:
                if previous_end < intervals[i][0]:
                    result.append(previous_end-previous_start+1)
                    previous_start, previous_end = intervals[i][0], intervals[i][1]            
                else:
                    previous_end=intervals[i][1]
        result.append(previous_end-previous_start+1)

        return result
   

        # 16%
        head, tail = 0, len(S)-1
        result, record = [], []
        cur = [-1, -1]
        while head<=tail:
            if S[head] in record:
                head+=1                                
            elif S[head]!=S[tail]:
                tail -=1                 
            else:
                if cur[1]<head:
                    result.append(cur[1]-cur[0]+1)
                    cur = [head, tail]
                    
                elif cur[1]<tail:
                    cur[1] = tail
                # else:                    
                    # continue
                record.append(S[tail])
                head+=1
                tail=len(S)-1
        
        result.append(cur[1]-cur[0]+1)
        del result[0]
        # for r in result:
        #     print(r)
        return result


        # 98%
        result=[]
        diction = {}
        for i in range(len(S)):
            diction[S[i]] = i

        head, tail = -1, 0   
        for i in range(len(S)):
            tail=max(diction[S[i]], tail)
            # print(tail)
            if i==tail:
                result.append(tail-head)
                head = tail
                
        return result         
