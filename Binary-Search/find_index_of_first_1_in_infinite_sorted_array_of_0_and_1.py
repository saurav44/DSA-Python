# same as find position of element in infinite sorted array

class Solution:
    def firstIndex(self, arr, n):

        # TC: O(log(p))
        # SC: O(1)

        low = 0
        high = 1

        while arr[high] == 0:
            low = high
            high = 2*high

        res = -1

        while (low <= high):
            mid = low + (high - low) // 2
            if arr[mid] == 1:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res


"""
Let p be the position of element to be searched. 
Number of steps for finding high index ‘h’ is O(Log p). The value of ‘h’ must be less than 2*p. 
The number of elements between h/2 and h must be O(p). 
Therefore, time complexity of Binary Search step is also O(Log p) and 
overall time complexity is 2*O(Log p) which is O(Log p).
"""