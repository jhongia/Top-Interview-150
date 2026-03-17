'''
226. Invert Binary Tree
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        tempLeft = root.left
        tempRight = root.right

        root.left = self.invertTree(tempRight)
        root.right = self.invertTree(tempLeft)
        return root
    
def printTree(root: Optional[TreeNode]):
    if root is None:
        return []
    return [root.val] + printTree(root.left) + printTree(root.right)
        
sol = Solution()
print(printTree(sol.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))))) # returns [4,7,2,9,6,3,1]
print(printTree(sol.invertTree(TreeNode(2, TreeNode(1), TreeNode(3))))) # returns [2,3,1]
print(printTree(sol.invertTree(None))) # returns []
