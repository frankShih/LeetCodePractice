class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A = sorted(A)
        '''
        # naive O(N^2), timeout
        result=[None]*len(A)
        visit = set()
        for i in range(len(B)):
            for j in range(len(A)):
                if not j in visit and A[j]>B[i]:
                    # print(A[j], B[i])
                    result[i]=A[j]
                    visit.add(j)
                    break

        for i in range(len(B)):
            if result[i] != None:
                continue
            for j in range(len(A)):
                if not j in visit:
                    # print(A[j], B[i])
                    result[i]=A[j]
                    visit.add(j)
                    break

        return result
        '''

        # O(Nlog(N)), greedy
        # create value:index mapping may lost the info. of duplicate values
        # so, create sorted indices
        sortIndB = sorted([x for x in range(len(B))], key=lambda x: B[x], reverse=True)
        # print(sortIndB)
        left, right = 0, len(A)-1
        result=[None]*len(A)

        for i in sortIndB:
            if A[right]>B[i]:
                result[i] = A[right]
                right-=1
            else:
                result[i] = A[left]
                left+=1

        return result