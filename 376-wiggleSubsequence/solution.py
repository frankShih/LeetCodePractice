class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length = len(nums)

        # DP + greedy (with memory optimized) O(N), 81%
        # longest sequence so far ending with rising/falling wiggle
        inc = dec = 1
        for i in range(length-1):
            if nums[i] > nums[i+1]:
                inc = dec + 1
            elif nums[i] < nums[i+1]:
                dec = inc + 1

        return max(inc, dec)
        '''

        # DP, 10% O(n^2)
        # longest sequence ending with rising/falling wiggle before index(i)
        dpUp, dpDown = [0]*length, [0]*length

        for i in range(1, length):
            for j in range(i):
                if nums[i]>nums[j]:
                    dpUp[i] = max(dpUp[i], dpDown[j]+1)
                elif nums[i]<nums[j]:
                    dpDown[i] = max(dpDown[i], dpUp[j]+1)

        return max(dpDown[-1], dpUp[-1])+1

        # naive solution, generate diffArray & check sign O(n). 91%
        diff = [0]*(length-1)
        for i in range(1, length):
            diff[i-1] = nums[i]-nums[i-1]
        # print(diff)

        startInd = 0
        while startInd< length-1 and not diff[startInd]:
            startInd+=1

        curr = startInd
        counter = 1 if startInd < length-1 else 0
        for i in range(startInd+1, length-1):
            if diff[curr]*diff[i]<0:
                # print(curr, i)
                counter+=1
                curr=i

        return counter+1
        '''
