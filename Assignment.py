def same_tweet_count(arr, size):

    dict = {}

    for i in range(0, size):
        dict[arr[i]] = dict.get(arr[i], 0) + 1
    return dict


# Driver Code
if __name__ == "__main__":
    test_case = int(input())

    for _ in range(test_case):
        arr = []
        size = int(input())
        for _ in range(size):
            lst = input().split()
            arr.append(lst[0])
        dict = same_tweet_count(arr, size)
        for i in sorted(dict.keys()):
            if dict[i] > 1:
                print(i,dict[i])

