# A naive recursive implementation of 0-1 Knapsack Problem


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


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50  # capacity W
n = len(val)
print(knapSack(W, wt, val, n))


# A Dynamic Programming based Python Program for 0-1 Knapsack problem
def knapSack(W, wt, val, n):
    # Build table K[][] in bottom up manner
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:  # item is too heavy to be hold
                K[i][w] = K[i-1][w]

    return K[n][W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
