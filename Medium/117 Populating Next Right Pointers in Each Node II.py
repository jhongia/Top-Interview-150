'''
117. Populating Next Right Pointers in Each Node II
Solved
Medium
Topics
premium lock icon
Companies
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

'''

import collections

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = collections.deque()

        if root is not None:
            q.append((root, 0))

        while len(q) > 0:
            node, currentLevel = q.popleft()

            if len(q) > 0:
                nextNode, nextNodeLevel = q[0]

                if currentLevel == nextNodeLevel:
                    node.next = nextNode

            for nextNode in [node.left, node.right]:
                if nextNode is not None:
                    q.append((nextNode, currentLevel + 1))

        return root
    
def print_via_next(root: 'Node'):
    if not root:
        return []
    ans = []
    level_start = root
    while level_start:
        node = level_start
        while node:
            ans.append(node.val)
            node = node.next
        ans.append('#')
        # find leftmost node of next level
        next_start = None
        n = level_start
        while n and next_start is None:
            next_start = n.left or n.right
            n = n.next
        level_start = next_start
    return ans

sol = Solution()
root = [1,2,3,4,5,None,7]
# Output[1,#,2,3,#,4,5,7,#]
print(print_via_next(sol.connect(Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7))))))