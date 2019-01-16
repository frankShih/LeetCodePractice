class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1

        length = len(nums)
        l, r = 0, length-1

        while l<=r:
            m = l+(r-l)//2
            # print(l, m, r)
            if nums[m]==target:
                return m

            if nums[m]<target:
                if nums[l]<=nums[m] or nums[l]>target:
                    l=m+1
                else:
                    r=m-1
            else:
                if nums[r] >= nums[m] or nums[r]<target:
                    r=m-1
                else:
                    l=m+1

        return -1