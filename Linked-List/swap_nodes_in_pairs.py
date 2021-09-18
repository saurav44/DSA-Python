# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:

        # TC: O(n)
        # SC: O(1)

        # prev -> a -> b -> b.next
        # prev -> b -> a -> b.next

        if head == None or head.next == None:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while (prev.next and prev.next.next):
            a = prev.next
            b = a.next

            prev.next, b.next, a.next = b, a, b.next

            # temp = b.next
            # b.next = a
            # prev.next = b
            # a.next = temp

            prev = a

        return dummy.next


