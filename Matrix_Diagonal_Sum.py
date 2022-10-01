class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        element_1 = int(n/2)
        print("e1", element_1)
        element_2 = int(n/2)
        print("e2", element_2)
        # res = n[element_1] + n[element_2]
        sum = 0
        for i in range(len(mat)):
            sum = sum + mat[i][i] + mat[i][n-1-i]
        print(sum)

        if n % 2 ==0:
            return sum

        else:
            sum = sum-mat[element_1][element_2]
            return sum