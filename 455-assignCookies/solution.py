class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 97%
        g = sorted(g)
        s = sorted(s)
        ind1, ind2 = 0, 0
        len_g, len_s = len(g), len(s)
        
        
        while ind1<len_g and ind2<len_s:
            # print(ind1,ind2)
            if g[ind1]<=s[ind2]:
                ind1+=1
                
            ind2+=1
            
        return ind1





