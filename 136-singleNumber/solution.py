class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        # naive solution O(N) 60%
        records = set()
        for n in nums:
            if not n in records:
                records.add(n)
            else:
                records.discard(n)

        return records.pop()
        '''

        # bitwise solution 98%
        result = 0
        for n in nums:
            result^=n

        return result