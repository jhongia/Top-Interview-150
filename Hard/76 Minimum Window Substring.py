'''
76. Minimum Window Substring
Hard
Topics
premium lock icon
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        left = 0
        min_length = float('inf')
        min_left = 0

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] -= 1

            while all(value <= 0 for value in count.values()):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left

                if s[left] in count:
                    count[s[left]] += 1

                left += 1

        return "" if min_length == float('inf') else s[min_left:min_left + min_length]


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t)) # "BANC"