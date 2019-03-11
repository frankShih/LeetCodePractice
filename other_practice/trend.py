'''

def solution(ranks):
    # write your code in Python 3.6
    if not ranks:
        return 0

    counts = dict()
    values = sorted(set(ranks)) # O(nlogn)

    for i in ranks:
        counts[i] = counts.get(i, 0) + 1

    result = 0
    for v in values:
        if v+1 in values:
            result+=counts[v]

    return result
'''


'''
def solution(A, B):
    # write your code in Python 3.6
    a, b = 'a', 'b'
    # if A/2 > B+1 or B/2 > A+1:
        # return ''

    result = []
    ind = 0
    if A == B:
        result = [a, b]*A
    elif A > B:
        result = [a, b]*B
        result.append(a)
        A -= (B+1)
        while A:
            result[ind] += a
            A -= 1
            ind += 2
    else:
        result = [b, a]*A
        result.append(b)
        B -= (A+1)

        while B:
            result[ind] += b
            B -= 1
            ind += 2

    return ''.join(result)


print(solution(2, 4))
'''


def solution(A):
    # write your code in Python 3.6
    price1, price7, price30 = [2, 7, 25]

    if not A:
        return 0

    length = len(A)
    if length >= 23:
        return price30

    '''
    # DP solution 1
    maxCost = [0]*(length+1)

    for i in range(1, length+1):
        one = maxCost[i-1]+price1    # set one-day cost

        j = i
        while j >= 0 and A[i-1]-A[j-1] < 7:
            j -= 1

        seven = price7
        if j >= 0:
            seven += maxCost[j]

        maxCost[i] = min(one, seven)

    # print(maxCost)
    '''
    # DP solution2
    maxCost = [0]*(31)

    for i in range(1, 31):
        if i in A:
            maxCost[i] = min(maxCost[i-1]+2, maxCost[i-7]+7)
        else:
            maxCost[i] = maxCost[i-1]

    # print([x for x in range(31)])
    # print(maxCost)
    # return min(maxCost[-1], price30)

    def helper(A, ind):
        if ind>=len(A):
            return 0

        # Make that choice
        # Explore it (the recursive step)
        # Un-choose (explore the other options)
        oneCost = 2+helper(A, ind+1)

        sevenInd = ind+1
        while sevenInd<len(A) and A[sevenInd]-A[ind]<7:
            sevenInd+=1

        sevenCost = 7+ helper(A, sevenInd)
        print(oneCost, sevenCost)
        return min(oneCost, sevenCost)


    return min(helper(A, 0), price30)



print(solution([1, 2, 3, 4, 7, 11, 12, 13]))  # 13
print(solution([1, 2, 3, 7, 8, 9, 11, 12, 13]))  # 13
print(solution([ 6, 7, 10, 11, 12, 13, 14, 17, 18  ]))  # 14
print(solution([1, 2, 3, 7, 9, 10, 11, 12, 16, 17, 18, 19, 22, 24, 26, 28]))
