# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []

        while head:
            list.append(head.val)
            head = head.next
        l, r = 0, len(list)-1

        if len(list) == 1:
            return True
        while l < r:
            if list[l] != list[r]:
                return False
            else:
                l+=1
                r-=1
        return True