1
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # time: O(N), space: O(N)

        s = sum(nums)
        n = len(nums)
        duplicate = s - sum(set(nums))
        missing = duplicate + int(((n*(n+1))/2)-s)
        return [duplicate, missing]

        '''
        # time: O(N), space: O(1)
        result = []
        length = len(nums)

        for i in range(length):
            ind = abs(nums[i])-1
            if nums[ind]>0:
                nums[ind]*=-1
            else:
                result.append(ind+1)

        print(nums)
        for i in range(length):
            # print(nums[i]-1)
            if nums[i]>0:
                result.append(i+1)
                break
        return result
        '''

        # time: O(N), space: O(1)
        len_n = len(nums)
        correct_sum = (len_n*(len_n+1))//2
        actual_sum = 0
        duplicate_num = 0
        
        for n in nums:
            real_idx = abs(n)-1
            if nums[real_idx] > 0: 
                nums[real_idx] *= -1
            else:
                duplicate_num = real_idx+1
            actual_sum += (real_idx+1)
        
        return [duplicate_num, correct_sum - (actual_sum - duplicate_num)]