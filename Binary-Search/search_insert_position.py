class Solution:
    def searchInsert(self, nums, target):

        # TC: O(log(n))
        # SC: O(1)

        n = len(nums)

        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return n

        low = 0
        high = n - 1

        while (low <= high):
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high -= 1
            else:
                low += 1

        # low will be at position where next greater element than target lies
        return low