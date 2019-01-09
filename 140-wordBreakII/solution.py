class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        '''
        # naive BFS, O(M*N^2), timeout
        Q = [[s, []]]
        result = []
        while Q:
            remain, path = Q.pop(0)

            if not remain:
                result.append(" ".join(path))
                continue

            length = len(remain)
            for i in range(length+1):
                if remain[:i] in wordSet:
                    Q.append([remain[i:], path+[remain[:i]]])

        return result
        '''

        DP recursive O(N*M^2)
        memo={}
        def go(s):
            if s in memo: return memo[s]
            if not s: return []
            ret = []
            for w in wordSet:
                if not s.startswith(w): continue
                elif len(w)==len(s): ret.append(w)
                else:
                    rest = go(s[len(w):])
                    print(w, rest)
                    for r in rest:
                        r = w + " " + r
                        ret.append(r)
                    
            memo[s] = ret
            return ret
        
        return go(s)
