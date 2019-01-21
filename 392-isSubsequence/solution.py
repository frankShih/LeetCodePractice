class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not(s): return True

        '''
        # naive forward searching O(max(N, M)), 81%
        lengthS = len(s)
        ind_s = 0

        for tt in t:
            if tt==s[ind_s]:
                ind_s+=1
                if ind_s==lengthS:   return True

        return False

        # naive forward searching O(N+M) 93%
        searchInd = -1
        for ss in s:
            searchInd = t.find(ss, searchInd+1)
            if searchInd == -1:
                return False
            # else:
                # t = t[searchInd+1:]

        return True
        '''

        # using iter-function O(M*N) 83%
        t = iter(t)
        return all(c in t for c in s)

