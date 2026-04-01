'''
54. Spiral Matrix
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_col = min_row = 0
        max_col, max_row = len(matrix[0]), len(matrix)
        row = 0
        answer = []

        while min_col < max_col and min_row < max_row:
            for col in range(min_col, max_col):
                answer.append(matrix[row][col])
            min_row += 1

            for row in range(min_row, max_row):
                answer.append(matrix[row][col])
            max_col -= 1

            if min_col < max_col and min_row < max_row:
                for col in range(max_col-1, min_col-1, -1):
                    answer.append(matrix[row][col])
                max_row -= 1

                for row in range(max_row-1, min_row-1, -1):
                    answer.append(matrix[row][col])
                min_col += 1

        return answer

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().spiralOrder(matrix)) # [1,2,3,6,9,8,7,4,5]