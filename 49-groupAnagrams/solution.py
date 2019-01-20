class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        if not strs:
            return []
        # using sorted strings as key to grouping 70% O(N*w*log(w))
        grouping = {}    
        sortStrs =  [tuple(sorted(x)) for x in strs]
        # print(sortStrs)
        for i in range(len(strs)):
            if not sortStrs[i] in grouping:
                grouping[sortStrs[i]] = [strs[i]]
            else:
                grouping[sortStrs[i]].append(strs[i])

        return [v for k, v in grouping.items()]            

        '''
        # samve method, more consice way
        d = {}
        for s in strs:
            k = tuple(sorted(s))
            d.setdefault(k, [])
            d[k].append(s)
        
        return[v for k, v in d.items()]
        '''


