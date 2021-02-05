def maxSumSubMatrix(arr, row, col):

    max = float("-inf")
    for left in range(col):
        temp = [0] * row
        for right in range(left,col):

            for i in range(row):

                temp[i] = temp[i] + arr[i][right]

            kadanemax = kadane(temp)

            if max < kadanemax:
                max = kadanemax
            else:
                continue
    return max

def kadane(arr):
    maxSoFar = arr[0]
    for num in arr[1:]:
        maxCurr = max(maxSoFar + num, num)
        maxSoFar = max(maxSoFar, maxCurr)

    return maxSoFar


arr = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

print(maxSumSubMatrix(arr, 4, 5))