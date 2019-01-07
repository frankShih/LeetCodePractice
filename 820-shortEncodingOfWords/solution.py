class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        

        words = list(set(words))
        '''
        naive solution, O(M*N^2)
        result = []
        if not words:
            return len(result)
            
        wordBank = {}
        for w in words:
            if not w[-1] in wordBank:
                wordBank[w[-1]] = []

            wordBank[w[-1]].append(w)
        # print(wordBank)
        
        for k, v in wordBank.items():
            v = sorted(v, key=lambda x: len(x), reverse=True)

            # print(v)
            visit = set()
            for v1 in v:
                if v1 in visit:
                    continue
                visit.add(v1)
                # print("current base", v1)
                for v2 in v:

                    if v1.endswith(v2):
                        visit.add(v2)
                        continue
                    
                result.append(v1)
            
        return sum([len(x)+1 for x in result])
        '''

        # optimize with set, O(MN)
        wordBank = set(words)

        for w in words:
            for i in range(1,len(w)):
                wordBank.discard(w[i:])
            
        return sum([len(x)+1 for x in wordBank])
