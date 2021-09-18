class Solution:
    def generateMatrix(self, n: int):

        # TC: O(n*n)
        # SC: O(n*n)

        m = n

        k = l = 0

        c = 1

        res = [[-1 for j in range(n)] for i in range(n)]

        while (k < m and l < n):

            for j in range(l, n):
                res[k][j] = c
                c += 1
            k += 1

            for i in range(k, m):
                res[i][n - 1] = c
                c += 1
            n -= 1

            if k < m:
                for j in range(n - 1, l - 1, -1):
                    res[m - 1][j] = c
                    c += 1
                m -= 1

            if l < n:
                for i in range(m - 1, k - 1, -1):
                    res[i][l] = c
                    c += 1
                l += 1

        return res