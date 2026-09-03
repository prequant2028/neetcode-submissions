# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        cur1 = head
        cur2 = head
        while cur2 and cur2.next:
            cur1 = cur1.next
            cur2 = cur2.next.next
        # Reverse second half
        curr = cur1.next
        cur1.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # Merge
        cur1 = head
        cur2 = prev
        while cur2:
            temp1 = cur1.next
            temp2 = cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1 = temp1
            cur2 = temp2