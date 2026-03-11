'''
61. Rotate List
Medium
Topics
premium lock icon
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

from torch import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        listNodeLength = 0
        rotated = 0

        if head == None:
            return None

        tail = None
        while curr:
            listNodeLength += 1
            if curr.next == None:
                tail = curr
            curr = curr.next
        
        if listNodeLength != 0:
            rotated = k % listNodeLength

        if rotated != 0:
            new_head = head
            new_tail = None
            tail.next = head
            steps_to_rotate = listNodeLength - rotated

            for i in range(steps_to_rotate):
                if i == steps_to_rotate - 1:
                    new_tail = new_head
                new_head = new_head.next

            head = new_head
            new_tail.next = None
        
        return head
    
def printList(head):
    while head:
        print(head.val, end = '->' if head.next else '')
        head = head.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
printList(head)
print('')
printList(Solution().rotateRight(head, 2))