class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # 20%
        if not(s): return True
        
        ind_s, ind_t = 0, 0
        
        while ind_t < len(t):
            if t[ind_t]==s[ind_s]:
                ind_s+=1
                if ind_s==len(s):   return True
                
            ind_t+=1
            
        return False     

        # 70%
        t = iter(t)
        return all(c in t for c in s)
    
        # 80%
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True
