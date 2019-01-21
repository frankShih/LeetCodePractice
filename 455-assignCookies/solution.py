class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)

        '''
        # naive greedy solution O(N+M), 97%
        ind1, ind2 = 0, 0
        len_g, len_s = len(g), len(s)

        while ind1<len_g and ind2<len_s:    # move break condition into loop
            # print(ind1,ind2)
            if g[ind1]<=s[ind2]:
                ind1+=1

            ind2+=1 # increasing each round, replace with loop

        return ind1
        '''

        # more concise form O(N), 91%
        ind = 0
        for size in s:
            if ind == len(g): break
            if g[ind] <= size : ind+=1

        return ind



