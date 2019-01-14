class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0

        length = len(tasks)

        '''
        # O(T^2)
        if not n :
            return length

        counting = [0]*26
        cooldown = [0]*26
        for t in tasks: counting[ord(t)-ord('A')]+=1
        # the job with most count, serve it first
        sorted(counting, reverse=True)

        remain = length
        currInd = 0
        while remain>0:
            for i in range(len(counting)):
                if cooldown[i]<=currInd and counting[i]:
                    counting[i]-=1
                    cooldown[i]+=n+1
                    remain-=1
                    break
            currInd+=1

        return currInd
        '''

        # O(T)
        counting = [0]*26
        for t in tasks: counting[ord(t)-ord('A')]+=1
        # find tha max-count job
        k = max(counting)
        taskNum = 0
        for c in counting:
            if c==k:
                taskNum+=1
        # 1. count==1, for each job
        # 2. at least (coolDown+1)*(maxJobCount-1) is needed,
        #    plus remaining tasks with same count

        return max(length, (n+1)*(k-1)+taskNum)
    