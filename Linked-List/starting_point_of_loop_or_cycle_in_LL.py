# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        # Time Complexity: O(N)
        # Space Complexity: O(1)

        # No cycle
        if head == None or head.next == None:
            return None

        fast = slow = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # There is no cycle
        if slow != fast:
            return None

        slow = head

        while (slow != fast):
            slow = slow.next
            fast = fast.next

        return slow