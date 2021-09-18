# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:

        # Time Complexity: O(n) + O(n-(k%n)) = O(n)
        # Space Complexity: O(1)

        if head == None or head.next == None or k == 0:
            return head

        # count
        cur = head
        n = 1
        while (cur.next != None):
            n += 1
            cur = cur.next
        # cur will be in last node

        # make cur point to head node
        cur.next = head

        # if k > n, we will rotate LL by k%n times
        k = k % n

        # move cur to position where we have to break link
        k = n - k

        while (k > 0):
            cur = cur.next
            k -= 1

        head = cur.next
        cur.next = None

        return head