
def maxSumSubsequence(arr):
    if not arr:
        return 0

    length = len(arr)
    best, curr = 0, 0
    # '''
    for i in range(length):
        # accumulate only when current value is positive
        if curr>0:
            curr+=arr[i]
        else:
            curr =arr[i] 
        best = curr if curr>best else best

    print("O(N) solution: ", best)  
    # '''

    taskQ = [[0, 0]]

    while taskQ:
        ind, curr = taskQ.pop(0)
        # print(ind, curr)
        if curr<0 or ind>length-1:
            continue
        
        taskQ.append([ind+1, curr+arr[ind]])
        taskQ.append([ind+1, 0])
        best = curr if curr>best else best
            
    print("O(N^2) solution: ", best)

data = [-2, 11, -4, 13, -2, 8]
maxSumSubsequence(data)            
