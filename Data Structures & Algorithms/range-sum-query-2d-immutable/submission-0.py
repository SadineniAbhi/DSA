class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pmat = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix) + 1)]

        # sum rows
        for i in range(1, len(self.pmat)):
            ps = 0
            for j in range(1, len(self.pmat[0])):
                temp = matrix[i-1][j-1]
                self.pmat[i][j] = ps + temp
                ps = ps + temp

        for j in range(1, len(self.pmat[0])):
            ps = 0
            for i in range(1, len(self.pmat)):
                temp = self.pmat[i][j]
                self.pmat[i][j] = ps + temp
                ps = ps + temp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pmat[row2+1][col2+1] - self.pmat[row2+1][col1] - self.pmat[row1][col2+1] + self.pmat[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)