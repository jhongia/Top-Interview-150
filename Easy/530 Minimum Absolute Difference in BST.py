'''

Code
Testcase
Testcase
Test Result
530. Minimum Absolute Difference in BST
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
 

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
'''

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = 0
        nodeValues = [root.val] if root else []
        level = []
        queue = [root]

        while queue != [] and root:
            for node in queue:
                if node.left:
                    level.append(node.left)
                    nodeValues.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    nodeValues.append(node.right.val)

            queue = level
            level = []
        
        nodeValues.sort()
        for i in range(len(nodeValues) - 1):
            if result == 0 or nodeValues[i+1] - nodeValues[i] < result:
                result = nodeValues[i+1] - nodeValues[i]
        return result

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(Solution().getMinimumDifference(root)) # 1