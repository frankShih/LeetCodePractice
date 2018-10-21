import math

class Solution:

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

'''
        # top-down, BFS
        # 26% after adding memory
        mark=[False]*(n+1)
        taskQueue=[[n, 0]]        #taskQueue=[[n, []]]
        
        while len(taskQueue)>0:
            # print(taskQueue)
            target, record = taskQueue.pop(0)            
            tmp=math.floor(math.sqrt(target))

            for i in range(tmp, 0, -1):
                remain = target-i**2
                # print(n, tmp, i, remain)

                if not(remain):
                    record+=1
                    return record
                else:
                    if mark[remain]: continue
                    mark[remain] = True
                    taskQueue.append([remain, record+1])
'''

    # bottom-up, dynamic programming
    dp_memory = [0]
    mark = [0]
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(self.dp_memory)<=n: 
            self.mark.extend([0]*(n-len(self.dp_memory)+1))
            self.dp_memory.extend([0]*(n-len(self.dp_memory)+1))
    
        for i in range(1, n+1):
            if not(self.mark[i]):
                candidate=float("inf")
                j=1
                j_2=j*j # assignment is much cheaper than multiplicaiton
                
                while i-j_2>=0:
                    candidate = min(candidate, self.dp_memory[i-j_2]+1)
                    j+=1
                    j_2=j*j
                self.dp_memory[i]=candidate
                self.mark[i]=1
            
        return self.dp_memory[n]
                    
'''
    # acceptable 60% solution (trick LC with caching)    
    _dp=[0]
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = self._dp
        while len(dp) <= n:
            candidate=[]
            for i in range(1, int(len(dp)**0.5+1)):
                candidate.append(dp[-i*i])
            dp += [min(candidate)+1]
            # dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
'''        