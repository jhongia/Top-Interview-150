'''
102. Binary Tree Level Order Traversal
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [[root.val]] if root else []
        level = []
        queue = [root]

        while queue != [] and root:
            levelValues = []
            for node in queue:
                if node.left:
                    level.append(node.left)
                    levelValues.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    levelValues.append(node.right.val)
            if levelValues != []:
                result.append(levelValues)
            queue = level
            level = []
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().levelOrder(root)) # [[3],[9,20],[15,7]]