# Solution 1

class Solution:
    def luckyNumbers(self, matrix):

        # TC: O(m*n)
        # SC: O(m + n)

        m = len(matrix)
        n = len(matrix[0])

        rowMin = []
        for i in range(m):
            mn = min(matrix[i])
            rowMin.append(mn)

        colMax = []
        for j in range(n):
            mx = 0
            for i in range(m):
                mx = max(mx, matrix[i][j])
            colMax.append(mx)

        ans = []
        for i in range(m):
            for j in range(n):
                if rowMin[i] == colMax[j]:
                    ans.append(rowMin[i])

        return ans



# *** Solution 2 *** using minMax and maxMin

import sys


class Solution:
    def luckyNumbers(self, matrix):

        # TC: O(m*n)
        # SC: O(1)

        m = len(matrix)
        n = len(matrix[0])

        # max of min among each row
        minMax = -sys.maxsize
        for i in range(m):
            mn = sys.maxsize
            for j in range(n):
                mn = min(mn, matrix[i][j])
            minMax = max(minMax, mn)

        # min of max among each column
        maxMin = sys.maxsize
        for j in range(n):
            mx = -sys.maxsize
            for i in range(m):
                mx = max(mx, matrix[i][j])
            maxMin = min(maxMin, mx)

        if minMax != maxMin:
            return []
        else:
            return [minMax]

