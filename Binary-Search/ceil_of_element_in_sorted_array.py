def findFloor( A, N, X):
    # Ceil: min of (larger element than X)

    # TC: O(log(n))
    # SC: O(1)

    low = 0
    high = N - 1
    res = -1
    while (low <= high):
        mid = low + ((high - low) // 2)
        if X == A[mid]:
            return mid
        elif X < A[mid]:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res