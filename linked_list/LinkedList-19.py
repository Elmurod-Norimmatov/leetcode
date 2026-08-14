# ACCEPTED

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr1 = dummy
        curr2 = dummy
        i = 0
        while curr1 and curr1.next:
            if i < n:
                curr1 = curr1.next
                i += 1
            else:
                curr1 = curr1.next
                curr2 = curr2.next

        curr2.next = curr2.next.next
        return dummy.next