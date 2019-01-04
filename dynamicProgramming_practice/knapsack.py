val = [40, 70, 130]
wt = [10, 20, 30]
nums = [3, 3, 3]
W = 50
n = len(val)

# naive recursive implementation of 0-1 Knapsack Problem
'''
def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    # weight of the nth item > Knapsack of capacity, W
    # this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))



print("knapSack recursive",knapSack(W, wt, val, n))
'''

# Dynamic Programming for 0-1 Knapsack problem
def knapSackZeroOne(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    '''
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:    # no item / weight
                K[i][w] = 0
            elif wt[i-1] <= w:
                # max value between: 
                # not taken item 'i' & take item 'i' with capacity reduce
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:  # item is too heavy to be hold
                K[i][w] = K[i-1][w]

    return K[n][W]
    '''

    # memory saving version (only use left&left-top box)
    K = [0 for x in range(W+1)]

    for i in range(n):
        # backward (need use left&left-top part)
        for j in range(W, wt[i]-1, -1):
            K[j] = max(val[i] + K[j-wt[i]],  K[j])
        
    return K[W]


print("knapSackZeroOne DP", knapSackZeroOne(W, wt, val, n))


# Dynamic Programming for 0-1 Knapsack problem with repetition
def knapSackUnbounded(W, wt, val, n):
    K = [0 for x in range(W+1)]
    for j in range(W+1):
        for i in range(n):
            if wt[i]<=j:
                # K[i][w] = max(val[i-1] + K[i][w-wt[i-1]],  K[i][w])
                K[j] = max(val[i] + K[j-wt[i]],  K[j])

    return K[W]


print("knapSackUnbounded DP", knapSackUnbounded(W, wt, val, n))


# A Dynamic Programming for Knapsack problem with limited amount of items
def knapSackBounded(W, wt, val, n, nums):
    K = [0 for x in range(W+1)]

    for i in range(n):
        num = min(nums[i], W//wt[i])
        selection = []  
        # treat it as 0/1 problem, for any 'n', can be represented as 2^x combination
        c = 1
        while num-c>=0:
            selection.append(c)
            c*=2
        print(num, selection)    
        for k in selection:
            print(W, wt[i], k)
            for j in range(W, wt[i]*k-1, -1):
                # max value between: 
                # not taken item 'i' & take item 'i' with capacity reduce
                K[j] = max(val[i]*k + K[j-wt[i]*k],  K[j])
    return K[W]

print("knapSackBounded DP", knapSackBounded(W, wt, val, n, nums))
