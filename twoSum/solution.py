class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        '''
        hashTable = {}  #value:index
        for i in range(len(nums)):
                     
            if hashTable.get(target-nums[i], None)!=None:
                
                return [hashTable[target-nums[i]], i]
            else:
                hashTable[nums[i]] = i
                 
        return []        
        '''
        
        sortN = nums[:]     #list(nums)
        sortN.sort()
        head, tail = 0, len(nums)-1
        
        while head<tail:
            sum = sortN[head]+sortN[tail]
            
            if sum<target:
                head+=1
            elif sum>target:
                tail-=1
            else:
                break
        
        result = []
        for i in range(len(nums)):
            if nums[i] == sortN[head] or nums[i] == sortN[tail]:
                result.append(i)
        
        return result