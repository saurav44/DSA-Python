class Solution:
    def firstIndex(self, arr, n):

        # TC: O(log(n))
        # SC: O(1)

        low = 0
        high = n - 1

        res = -1

        while (low <= high):
            mid = low + (high - low) // 2
            if arr[mid] == 1:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res