'''
73. Set Matrix Zeroes
Attempted
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = col_flag = False
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    if row == 0:
                        row_flag = True
                    if col == 0:
                        col_flag = True
                    elif row != 0 and col != 0:
                        matrix[row][0] = 0
                        matrix[0][col] = 0
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if row_flag:
            matrix[0] = [0] * cols
        if col_flag:
            for row in range(rows):
                matrix[row][0] = 0

sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)
print(matrix) # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
