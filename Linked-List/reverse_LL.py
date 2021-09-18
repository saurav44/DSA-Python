# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):

        # TC: O(n)
        # SC: O(1)

        cur = head
        prev = None
        while (cur != None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head = prev
        return head