# Same as find first and last element in sorted array
# return lastPos - firstPos + 1

class Solution:

    # TC: O(log(n)) + O(log(n))
    # SC: O(1)

    def searchFirst(self, nums, target, low, high):
        res = -1
        while (low <= high):
            mid = low + ((high - low) // 2)
            if target == nums[mid]:
                res = mid
                high = mid - 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return res

    def searchLast(self, nums, target, low, high):
        res = -1
        while (low <= high):
            mid = low + ((high - low) // 2)
            if target == nums[mid]:
                res = mid
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return res

    def searchRange(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1
        low = 0
        high = n - 1
        first = self.searchFirst(nums, target, low, high)
        last = self.searchLast(nums, target, low, high)

        return last-first+1