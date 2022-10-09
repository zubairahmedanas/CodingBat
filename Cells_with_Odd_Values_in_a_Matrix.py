class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = []
        count = 0
        for i in range(m):
            mat = []
            for j in range(n):
                mat.append(0)
            # print("the mat is", mat)
            matrix.append(mat)
        # print("the mat is", matrix)

        for r, c in indices:
            for k in range(n):
                matrix[r][k] += 1
            for z in range(m):
                matrix[z][c] += 1
        # print("matrix -",  matrix)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 == 1:
                    count += 1

        return count

