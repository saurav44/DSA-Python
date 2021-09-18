# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):

        # TC: O(n)
        # SC: O(1)

        if head == None:
            return None

        fast = slow = head

        for i in range(n):
            fast = fast.next

        # This handles the edge case i.e if there are 5 nodes and n = 5
        if fast == None:
            head = head.next
            return head

        while (fast.next != None):
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head