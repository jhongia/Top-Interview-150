'''
228. Summary Ranges
Easy
Topics
premium lock icon
Companies
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
'''

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        startNum = 0
        seq = 1
        count = 0
        toapd = ""

        for num in nums:
            if count == 0:
                startNum = num
                count += 1
                toapd = str(startNum)
                if len(nums) == 1:
                    out.append(toapd)
                    break
            elif num > startNum and count > 0 and num - startNum == seq:
                if num == nums[-1]:
                    toapd += "->" + str(num)
                    out.append(toapd)
                count += 1
                startNum = num
            elif num > startNum and count > 0 and num - startNum != seq:
                if str(startNum) != toapd[-1] and str(startNum) != toapd:
                    toapd += "->" + str(startNum)
                out.append(toapd)
                startNum = num
                toapd = str(num)
                if num == nums[-1]:
                    out.append(toapd)
                count += 1

        return out
    
sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7])) # ["0->2","4->5","7"]