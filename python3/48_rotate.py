48.旋转图像
class Solution1:
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        return matrix
