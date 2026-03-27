'''
222. Count Complete Tree Nodes
Easy
Topics
premium lock icon
Companies
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def lheight(node):
            if not node:
                return 0
            return 1 + lheight(node.left)

        def rheight(node):
            if not node:
                return 0
            return 1 + rheight(node.right)

        l,r = lheight(root), rheight(root)

        if l > r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return (2 ** l) - 1
        
sol = Solution()
print(sol.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))    # return 6
print(sol.countNodes(None))    # return 0
print(sol.countNodes(TreeNode(1)))    # return 1

