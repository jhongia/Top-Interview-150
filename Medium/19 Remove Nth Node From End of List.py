'''
19. Remove Nth Node From End of List
Medium
Topics
premium lock icon
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
'''

from torch import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev, curr = dummy, dummy
        for i in range(n + 1):
            curr = curr.next

        while curr:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next

        return dummy.next
    
# Add this helper function after the Solution class
def print_list(head):
    current = head
    while current:
        print(current.val, end='->' if current.next else '')
        current = current.next
    print()

# Example usage:
# Creating a linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("Original list:")
print_list(head)
sol = Solution()
new_head = sol.removeNthFromEnd(head, 2)
print("List after removing 2nd node from the end:")
print_list(new_head)