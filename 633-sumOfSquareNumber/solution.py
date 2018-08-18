class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        '''
        # 30%
        candidate=[]
        for i in range(int(c**0.5)+1):
            # candidate.append(i**2)
            temp = (c-i**2)**0.5
            if temp == round(temp): 
                return True
            
        # for can in candidate:
        #     if c-can in candidate:
        #         return True
            
        return False    
        '''

        
        # 50%
        for i in range(int(c**0.5)+1):
        
            temp = (c-i**2)**0.5
            if temp == round(temp): 
                return True
            
        return False
        
