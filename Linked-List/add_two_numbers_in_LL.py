# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Time Complexity: O(max(n1,n2))
        # Space Complexity: O(n) i.e sum

        dummy = ListNode()
        temp = dummy

        carry = 0

        while (l1 != None) or (l2 != None) or (carry != 0):
            sm = 0

            if l1 != None:
                sm += l1.val
                l1 = l1.next

            if l2 != None:
                sm += l2.val
                l2 = l2.next

            sm += carry

            # carry is n//10 ie 15//10 = 1
            carry = sm // 10

            # remainder is n % 10
            newNode = ListNode(sm % 10)

            temp.next = newNode
            temp = temp.next

        return dummy.next

