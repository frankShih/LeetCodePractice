class Solution(object):
    def init_list_of_objects(self, size):
        # create empty list of list
        list_of_objects = list()
        for i in range(0,size):
            list_of_objects.append( list() ) #different object reference each time
        return list_of_objects


    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        '''

        # O(N+26*2) 72%
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
                intervals.append([c[0], c[-1]])

        # convret it to "number of non-overlap intervals" problem
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

        '''

        # keep the last occured index O(2N), 60%
        result=[]
        lastIndice = [0]*26
        length = len(S)
        for i in range(length):
            lastIndice[ord(S[i])-97] = i

        head, tail = -1, 0
        for i in range(length):
            tail = max(lastIndice[ord(S[i])-97], tail)
            # print(tail)
            if i==tail:
                # the last index of all nums seen before <= i
                result.append(tail-head)
                head = tail

        return result
