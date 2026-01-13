'''
Docstring for Easy.58 Length of Last Word
58. Length of Last Word
Attempted
Easy
Topics
premium lock icon
Companies
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = ""
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] != " ":
                ans += s[i]
            elif len(ans) > 0 and s[i] == " ":
                break
        return len(ans)
    
sol = Solution()
s = "a "
print(sol.lengthOfLastWord(s)) # 1