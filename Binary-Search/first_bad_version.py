# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):

        # TC: O(log(n))
        # SC: O(1)

        low = 1
        high = n

        res = -1

        while (low <= high):
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res