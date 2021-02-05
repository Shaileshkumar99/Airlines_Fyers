def MaxSumSubSetNoAdjency(arr):
    if not len(arr):
        return
    elif len(arr) == 1:
        return arr[0]

    maxSum = arr[:]
    maxSum[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        maxSum[i] = max(maxSum[i-1], maxSum[i-2]+arr[i])

    return maxSum[-1]