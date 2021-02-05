# find maximum sum of subarray

def kadanesAlgo(arr):
    maxCurr = arr[0]
    maxSoFar = arr[0]
    for num in arr[1:]:
        maxCurr = max(maxSoFar + num, num)
        maxSoFar = max(maxSoFar, maxCurr)

    return maxSoFar