'''
22. Generate Parentheses
Solved
Medium
Topics
premium lock icon
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(o, c, curr):
            if o == c == 0:
                result.append(curr)
                return
            
            if o > 0:
                generate(o-1, c, curr + "(")
            if o < c:
                generate(o, c-1, curr + ")")
        generate(n, n, "")

        return result
    
n = 3
print(Solution().generateParenthesis(n)) # ["((()))","(()())","(())()","()(())","()()()"]