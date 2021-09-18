# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:

        # Time Complexity: O(n/k)*O(k) = O(n) i.e no.of groups * k iteration
        # Space Complexity: O(1)

        # if head is Null or k is 1
        if head == None or k == 1:
            return head

        dummy = ListNode()
        dummy.next = head

        prev = cur = nxt = dummy

        # count
        c = 0

        cur = head
        while (cur != None):
            cur = cur.next
            c += 1

        # n//k groups will be reversed
        while (c >= k):
            cur = prev.next
            nxt = cur.next

            # for k we have to reverse k-1 links
            for i in range(1, k):
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = cur.next

            prev = cur
            c -= k

        return dummy.next
