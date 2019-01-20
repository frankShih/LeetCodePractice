class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        '''
        strCount = len(strs)
        result = ''
        if strCount == 0:
            return result
        
        # O(N*M^2), backward checking
        minstring = min(strs, key=lambda x: len(x))
        length = len(minstring)

        while length > 0:
            found = True
            substring = minstring[:length]
            for i in range(strCount):
                if not strs[i].startswith(substring):
                    found = False
                    break
            if found:
                break
            length -= 1
        return minstring[:length]
        
        # naively go through all strings at ind[i] O(M*N)
        def match(strs, ind):
            for s in strs:
                if ind > len(s)-1:
                    return False
                if s[ind] != strs[0][ind]:
                    return False
            return True

        for i in range(len(strs[0])):
            if match(strs, i):
               result += strs[0][i]
            else:
                break
        return result
        '''
        
        # much more consice solution O(N*M)
        ret=""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                ret += chars[0]
            else:
                return ret
        return ret