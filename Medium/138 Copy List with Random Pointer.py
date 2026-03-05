'''
138. Copy List with Random Pointer
Medium
Topics
premium lock icon
Companies
Hint
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
'''

# Definition for a Node.
from torch import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        currentNode = head
        mapping = {}
        counter = 0

        while currentNode:
            mapping[currentNode] = Node(currentNode.val)
            currentNode = currentNode.next
        
        currentNode = head
        while currentNode:
            copy = mapping[currentNode]
            copy.next = mapping[currentNode.next] if currentNode.next else None
            copy.random = mapping[currentNode.random] if currentNode.random else None
            currentNode = currentNode.next

        return mapping[head] if head else None
        
sol = Solution()
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1
copy = sol.copyRandomList(node1)
print(copy.val) # 7
print(copy.next.val) # 13
print(copy.next.next.val) # 11
print(copy.next.next.next.val) # 10
print(copy.next.next.next.next.val) # 1 