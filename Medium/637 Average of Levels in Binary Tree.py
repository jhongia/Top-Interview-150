'''
637. Average of Levels in Binary Tree
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = [root.val] if root is not None else []
        level = []
        queue = [root]

        while queue != [] and root:
            avg = 0
            avgCount = 0
            for node in queue:
                if node.left:
                    level.append(node.left)
                    avg += node.left.val
                    avgCount += 1
                if node.right:
                    level.append(node.right)
                    avg += node.right.val
                    avgCount += 1

            if avgCount != 0:
                result.append(avg/avgCount)
            queue = level
            level = []
        return result
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().averageOfLevels(root)) # [3.00000,14.50000,11.00000]