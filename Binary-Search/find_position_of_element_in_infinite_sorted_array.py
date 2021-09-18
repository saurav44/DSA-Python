# Same as binary search but we need to find the high value
# Let p be the position of element to be searched. Number of steps for finding high index ‘h’ is O(Log p)
# overall time complexity is 2*O(Log p) which is O(Log p).

class Solution:
    def search(self, nums, target):

        # TC: O(log(p))
        # SC: O(1)

        low = 0
        high = 1

        # if target greater than higher value, it means we need to increase the value of high
        while target > nums[high]:
            low = high
            high = 2*high

        while (low <= high):
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1