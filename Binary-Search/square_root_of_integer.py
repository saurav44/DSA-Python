class Solution:
    def mySqrt(self, x: int) -> int:

        # TC: O(log(n))
        # SC: O(1)

        low = 0
        high = x
        res = -1
        while(low <= high):
            mid = low + (high - low)//2
            if mid*mid <= x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res