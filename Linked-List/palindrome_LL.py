# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):
        if head == None or head.next == None:
            return head

        prev = None
        cur = head

        while (cur != None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    def isPalindrome(self, head: ListNode) -> bool:

        # Time Complexity: O(n/2) + O(n/2) + O(n/2) i.e middle + rev + dummy
        # Space Complexity: O(n)

        # no node or single node
        if head == None or head.next == None:
            return True

        fast = slow = head

        # find middle element i.e left middle if even
        while (fast.next != None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next

        # reverse after slow
        slow.next = self.reverse(slow.next)

        slow = slow.next

        # check if nodes from first and slow are equal
        while (slow != None):
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True

