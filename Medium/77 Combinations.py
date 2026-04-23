'''
77. Combinations
Medium
Topics
premium lock icon
Companies
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, sol = [], []

        def backtrack(x):
            if len(sol) == k:
                ans.append(sol[:])
                return
            
            left = x
            still_need = k - len(sol)

            if left > still_need:
                backtrack(x-1)
            
            sol.append(x)
            backtrack(x-1)
            sol.pop()

        backtrack(n)
        return ans
    
n = 4
k = 2
print(Solution().combine(n, k)) # [[2,1],[3,1],[3,2],[4,1],[4,2],[4,3]]