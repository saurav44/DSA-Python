class Solution:
    def spiralOrder(self, matrix):

        # TC: O(m*n)
        # SC: O(m*n)

        m = len(matrix)
        n = len(matrix[0])

        k = l = 0

        spiral = []
        while (k < m and l < n):

            for j in range(l, n):
                spiral.append(matrix[k][j])
            k += 1

            for i in range(k, m):
                spiral.append(matrix[i][n - 1])
            n -= 1

            if (k < m):

                for j in range(n - 1, l - 1, -1):
                    spiral.append(matrix[m - 1][j])
                m -= 1

            if (l < n):

                for i in range(m - 1, k - 1, -1):
                    spiral.append(matrix[i][l])
                l += 1

        return spiral