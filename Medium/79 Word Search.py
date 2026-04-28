'''
79. Word Search
Medium
Topics
premium lock icon
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        W = len(word)

        if m == 1 and n == 1:
            return board[0][0] == word
        
        def backtrack(pos, index):
            i, j = pos

            if index == W:
                return True

            if board[i][j] != word[index]:
                return False

            char = board[i][j]
            board[i][j] = '#'
            for i_off, j_off in [(0,1), (1,0), (0,-1), (-1,0)]:
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n:
                    if backtrack((r,c), index+1):
                        return True

            board[i][j] = char
            return False

        for i in range(m):
            for j in range(n):
                if backtrack((i,j), 0):
                    return True

        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(Solution().exist(board, word)) # true