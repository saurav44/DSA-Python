class Solution:
    def nextGreatestLetter(self, letters, target):

        n = len(letters)

        low = 0
        high = n - 1

        res = ''
        while (low <= high):
            mid = low + (high - low) // 2
            if target == letters[mid]:
                low = mid + 1
            elif target < letters[mid]:
                res = letters[mid]
                high = mid - 1
            else:
                low = mid + 1

        if res == '':
            # letters does not contain character greater than target
            # so return first character
            return letters[0]
        else:
            return res