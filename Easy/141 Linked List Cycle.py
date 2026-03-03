'''
141. Linked List Cycle
Easy
Topics
premium lock icon
Companies
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?


'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list_with_cycle(arr, pos):
    if not arr:
        return None

    nodes = []
    # 1. Create all nodes
    for val in arr:
        nodes.append(ListNode(val))

    # 2. Link nodes sequentially
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]

    # 3. Create the cycle
    if pos != -1:
        # The last node (tail) points to the node at the specified position
        nodes[-1].next = nodes[pos]
        
    return nodes[0] # Return the head of the list

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        currentNode = head

        while currentNode:
            if id(currentNode) in visited:
                return True

            visited.add(id(currentNode))    
            currentNode = currentNode.next

        return False
    
solution = Solution()
data = [3, 2, 0, -4]
head_node = create_linked_list_with_cycle(data, 1) # Create a cycle at index 1
print(solution.hasCycle(head_node)) # Output: True