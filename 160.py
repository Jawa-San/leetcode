# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = headA
        listB = headB
        while listA:
            while listB:
                if listA == listB:
                    return listA
                else:
                    listB = listB.next
            listB = headB
            listA = listA.next
        return None
            
        