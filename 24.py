# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        resHead = res
        curr = head
        if curr is None or curr.next is None:
            return head

        while curr:
            if curr.next is not None:
                res.next = ListNode(curr.next.val)
                res = res.next
            res.next = ListNode(curr.val)
            res = res.next
            if curr.next is None:
                return resHead.next
            curr = curr.next.next
        return resHead.next