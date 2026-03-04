'''
21. Merge Two Sorted Lists
Easy
Topics
premium lock icon
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(lst):
    nodes = []

    for num in lst:
        nodes.append(ListNode(num))

    for i in range(len(lst) - 1):
        nodes[i].next = nodes[i + 1]
    
    return nodes[0]

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergeList = []
        
        if not list1 and not list2:
            return list1
            
        while list1:
            mergeList.append(list1.val)
            list1 = list1.next
        
        while list2:
            mergeList.append(list2.val)
            list2 = list2.next

        mergeList.sort()

        return createLinkedList(mergeList)
    
sol = Solution()
list1 = createLinkedList([1,2,4])
list2 = createLinkedList([1,3,4])
result = sol.mergeTwoLists(list1, list2)
while result:
    print(result.val)
    result = result.next