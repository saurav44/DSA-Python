# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: [ListNode]) -> [int]:

        # TC: O(n) + O(n) => one for loop and another for stack push and pop
        # SC: O(n)

        arr = []

        cur = head
        while (cur):
            arr.append(cur.val)
            cur = cur.next

        n = len(arr)

        st = []
        res = [0] * n

        for i in range(n - 1, -1, -1):
            while (len(st) > 0 and st[-1] <= arr[i]):
                st.pop()

            if len(st) != 0:
                res[i] = st[-1]

            st.append(arr[i])

        return res
