class Solution(object):
    def uniquePaths(self):

        # m : (int) rows
        # n : (int) cols

       #mat = [[0] * ncols] * ncols
        #mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        mat = [[1, 1], [0, 1]]

        nrows=len(mat)
        ncols=len(mat[0])

        #print(mat)
        #for i in range(ncols):
        #    mat[0][i] = 1

        #print(mat)
        #for i in range(nrows):
        #    mat[i][0] = 1

        print(mat)

        for rIdx in range(1,nrows):
            for cIdx in range(1,ncols):
                mat[rIdx][cIdx] = mat[rIdx - 1][cIdx] + mat[rIdx][cIdx - 1]

        print(mat)

        return mat[nrows - 1][ncols - 1]

sol = Solution()
print(sol.uniquePaths())