import sys
def maxSumSubmatrix(matrix):
    if not matrix or not matrix[0]:
        return 0

    row, col = len(matrix), len(matrix[0])
    best = -1*sys.maxsize

    for i in range(row):
        dp = [0]*col
        for j in range(i, row):
            curr = 0
            for k in range(col):
                # dp[k:] - sum from row 'i~j-1' & col 'k:'
                # dp[:k] - sum from row 'i~j' & col ':k'
                # transform 2-d matrix to maxSumSubsequence problem 
                dp[k] += matrix[j][k]
                curr += dp[k]
                if curr<0:
                    curr = dp[k]
                best = curr if curr>best else best

    print("O(N^3) solution: ", best)  

    
data = [[0, -2, -7, 0],[9, 2, -6, 2], [-4, 1, -4, 1], [-1, 8, 0, -2], [1, 2, 3, 4]]
maxSumSubmatrix(data)            
