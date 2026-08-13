# ACCEPTED

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        n = 0
        while l1 or l2:
            if l1 and l2:
                res = l1.val + l2.val + n
                l1 = l1.next
                l2 = l2.next
            elif l1:
                res = l1.val + n
                l1 = l1.next
            elif l2:
                res = l2.val + n
                l2 = l2.next

            n = res // 10
            curr.next = ListNode(res%10)
            curr = curr.next

        if n == 1:
            curr.next = ListNode(n)

        return dummy.next