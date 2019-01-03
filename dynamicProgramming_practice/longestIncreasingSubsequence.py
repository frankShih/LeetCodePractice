# Dynamic programming of longest increasing subsequence, O(n^2)


def lis(arr):
    n = len(arr)
    # dp: length of the LIS before index_i
    dp = [1]*n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


arr = [10, 22, 9, 33, 21, 50, 41, 60, 0, 0, 33, 55, 77, 99]
print("Length of lis is", lis(arr))


# recirsive version, O(n^2)??
def lisRes(arr):
    length = len(arr)

    def helper(cur, ind):
        if ind == length:
            return 0

        if arr[ind] > cur:
            return helper(arr[ind], ind+1)+1
        else:
            return helper(cur, ind+1)

    best = 0
    for i in range(length):
        temp = helper(arr[i], i)+1
        print(i, temp)
        if temp > best:
            best = temp

    return best


print("Length of lis is", lisRes(arr))


def lengthOfLIS(nums):
    # brute force O(n^3)
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0
    length = len(nums)

    cands = []
    ind = 0

    while ind < length:
        for i in range(len(cands)):
            if cands[i][-1] < nums[ind]:
                cands.append(cands[i]+[nums[ind]])
        cands.append([nums[ind]])
        ind += 1
    # print(cands)

    best = 1
    for c in cands:
        best = len(c) if len(c) > best else best

    return best


print(lengthOfLIS(arr))
