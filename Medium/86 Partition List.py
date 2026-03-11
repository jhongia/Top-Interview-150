'''
86. Partition List
Medium
Topics
premium lock icon
Companies
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

from torch import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        prevListNode = None
        afterListNode = None
        tailPrevListNode = None
        tailafterListNode = None

        while curr:
            temp = curr.next
            if curr.val < x:
                if prevListNode == None:
                    prevListNode = curr
                    tailPrevListNode = prevListNode
                else:
                    tailPrevListNode.next = curr
                    tailPrevListNode = curr
                
            else:
                if afterListNode == None:
                    afterListNode = curr
                    tailafterListNode = afterListNode
                else:
                    tailafterListNode.next = curr
                    tailafterListNode = curr
                
            if tailafterListNode:
                tailafterListNode.next = None
            curr = temp
        
        if tailPrevListNode:
            tailPrevListNode.next = afterListNode
            head = prevListNode
        else:
            head = afterListNode
                
        return head
    
def printList(head):
    curr = head
    while curr:
        print(curr.val, end = '->' if curr.next else '')
        curr = curr.next

ListNode1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
printList(ListNode1)
print('')
printList(Solution().partition(ListNode1, 3))

