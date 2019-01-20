class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # using list for mapping to get better performance
        arrS = [None]*128
        arrT = [None]*128

        for i in range(len(s)):
            # give each mapping pair a number(as ID)
            poS = ord(s[i])  # map from char(poS in arrS) to char(i in t)
            poT = ord(t[i])

            if arrS[poS] != arrT[poT]:
                return False

            if not(arrS[poS]):
                arrS[poS], arrT[poT] = i, i

        return True
        
        '''
        # keep mapping in dict, concise solution
        found = {}

        for i in range(len(s)):
            if s[i] in found:
                if not found[s[i]] == t[i]:
                    return False
            else:
                if t[i] in found.values():
                    return False
                found[s[i]] = t[i]
    
        return True      
        '''
