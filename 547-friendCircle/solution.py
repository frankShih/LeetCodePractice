class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """


'''
        # 45%
        counter=0
        check=[0]*len(M)

        def helper(ind):
            check[ind]=1
            for j in range(0, len(M[0])):
                if M[ind][j] and not(check[j]):
                    helper(j)

        for i in range(len(M)):
            if not(check[i]):
                helper(i)
                counter+=1

        return counter
'''
    # 40%
  cand = [set([ind for ind, x in enumerate(m) if x == 1]) for m in M]
   # print(cand)
   while True:
        checker = 0
        for i in range(len(M)-1):
            for j in range(i+1, len(M)):
                if not(cand[i]) or not(cand[j]):
                    continue
                if cand[i] & cand[j]:
                    checker = 1
                    cand[i] |= cand[j]
                    cand[j] = set()
        if not(checker):
            break

    counter = 0

    for c in cand:
        if c:
            counter += 1

    return counter
