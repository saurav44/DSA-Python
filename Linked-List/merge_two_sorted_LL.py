# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):

        # Time Complexity: O(n1 + n2)
        # Space Complexity: O(1)
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        # lesser one will be l1
        if l2.val < l1.val:
            l1, l2 = l2, l1

        res = l1

        while l1 != None and l2 != None:
            temp = None
            while l1 != None and l1.val <= l2.val:
                temp = l1
                l1 = l1.next

            # when l1 not less than l2
            temp.next = l2

            l1, l2 = l2, l1

        return res