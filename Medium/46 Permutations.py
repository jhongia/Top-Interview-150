'''
46. Permutations
Solved
Medium
Topics
premium lock icon
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans


nums = [1,2,3]
print(Solution().permute(nums)) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]