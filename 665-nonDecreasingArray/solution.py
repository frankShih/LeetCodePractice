class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        # 80%
        seq = []
        cur = float('-inf')
        temp = []
        
        for i in range(len(nums)):
            if nums[i]>=cur:
                temp.append(nums[i])                
            else:
                seq.append(temp)
                if len(seq)>1: return False
                temp=[nums[i]]
                
            cur=nums[i]    
        seq.append(temp)
        
        # print(seq)
        
        if len(seq)<2: return True
        if len(seq[0])==1 or seq[0][-2]<seq[1][0]: return True
        if len(seq[1])==1 or seq[0][-1]<seq[1][1]: return True
            
        return False