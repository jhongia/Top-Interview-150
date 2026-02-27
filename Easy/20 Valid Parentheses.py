'''
20. Valid Parentheses
Attempted
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        answer = False
        stack = []

        if len(s) % 2 == 0 and (s[0] == "(" or s[0] == "[" or s[0] == "{"):
            for char in s:
                if char == "(" or char == "[" or char == "{":
                    stack.append(char)
                elif (char == ")" or char == "]" or char == "}") and stack != []:
                    if char == ")" and stack[-1] == "(":
                        stack.pop()
                    elif char == "]" and stack[-1] == "[":
                        stack.pop()
                    elif char == "}" and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            if stack == []:
                answer = True
                
        return answer

sol = Solution()
print(sol.isValid("()")) # True