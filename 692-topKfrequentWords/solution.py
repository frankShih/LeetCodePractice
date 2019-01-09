class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        result = []

        if not words or not k:
            return result
        
        length = len(words)

        # O(N)naive solution, 40%
        counter = dict()
        for w in words:
            if w not in counter:
                counter[w]=0
            counter[w]+=1

        # print(counter)

        revCounter = dict()

        for e, v in counter.items():
            if not v in revCounter:
                revCounter[v]=[]
            
            revCounter[v].append(e)

        # print(revCounter)
        
        ind = 0
        for i in range(length, 0, -1):
            if i in revCounter:
                result.extend(sorted(revCounter[i]))
                ind+=len(revCounter[i])

            if ind>=k:
                break

        return result[:k]        
        