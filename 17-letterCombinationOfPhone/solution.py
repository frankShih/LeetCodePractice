class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not(digits): return []
        mapping = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}

        '''
        
        # BFS 60%
        def genString(newList, currList):
            if not(currList):
                currList.extend(newList)
                return
            size = len(currList)
            for i in range(size):
                temp = currList.pop(0)
                for j in newList:
                    currList.append(temp+j)
        
        queue = list(digits)
        result = []
        
        while queue:
            temp = queue.pop(0)
            genString(mapping[temp], result)

        return result    

        # BFS, same speed, more clean
        int2char = {'1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []
        for i in digits:
            if not res:
                res = int2char[i]
            else:
                res = [j+k for j in res for k in int2char[i]]
        return res
        '''

        