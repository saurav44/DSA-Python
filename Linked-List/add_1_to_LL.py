"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """

    def reverse(self, head):

        if head == None or head.next == None:
            return head

        cur = head
        prev = None

        while (cur != None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def plusOne(self, head):
        # Write your code here

        l1 = self.reverse(head)

        l2 = ListNode(1)

        dummy = ListNode(-1)
        temp = dummy

        carry = 0
        while l1 != None or l2 != None or carry != 0:
            sm = 0
            if l1 != None:
                sm += l1.val
                l1 = l1.next

            if l2 != None:
                sm += l2.val
                l2 = l2.next

            sm += carry

            carry = sm // 10

            newNode = ListNode(sm % 10)
            temp.next = newNode
            temp = temp.next

        head = dummy.next
        res = self.reverse(head)

        return res
