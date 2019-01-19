class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return [0]

        length = len(T)
        result = [0]*length

        '''
        # naive solution O(N^2), timeout
        for i in range(length):    
            for j in range(i, length):    
                if T[i]<T[j]:
                    result[i] = j-i
                    break
        '''

        # stack solution, O(N)
        indQ = []
        for i in range(length):    
            # keep in memory & traverse backward when condition satisfied
            while indQ and T[indQ[0]] < T[i]:
                result[indQ[-1]] = i-indQ[0]
                indQ.pop()

            indQ.append(i)
        
        return result