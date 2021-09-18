# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        # Time Complexity: O(2m) where m is length of larger LL
        # Space Complexity: O(1)

        if headA == None or headB == None:
            return None

        a = headA
        b = headB

        while (a != b):

            if a != None:
                a = a.next
            elif a == None:  # if a is Null, it points to headB
                a = headB

            if b != None:
                b = b.next
            elif b == None:  # if b is Null, it points to headA
                b = headA

        return a

