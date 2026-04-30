'''
148. Sort List
Medium
Topics
premium lock icon
Companies
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        nums.sort()
        node = ListNode()
        currNode = node

        for num in nums:
            currNode.next = ListNode(num)
            currNode = currNode.next

        return node.next

head = [4,2,1,3]
node = ListNode()
currNode = node

for num in head:
    currNode.next = ListNode(num)
    currNode = currNode.next

newNode = Solution().sortList(node.next)
output = ""
while newNode:
    output += str(newNode.val) + "->" if newNode.next else str(newNode.val)
    newNode = newNode.next
print(output) # 1->2->3->4