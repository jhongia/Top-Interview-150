'''
103. Binary Tree Zigzag Level Order Traversal
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [[root.val]] if root else []
        level = []
        queue = [root]
        even = True
        
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
                if even:
                    result.append(levelValues[::-1])
                    even = False
                else:
                    result.append(levelValues)
                    even = True
            queue = level
            level = []
        return result
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().zigzagLevelOrder(root)) # [[3],[20,9],[15,7]]