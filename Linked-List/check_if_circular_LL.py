def isCircular(head):
    # TC: O(n)
    # SC: O(1)

    if head == None or head.next == head:
        return True

    cur = head

    while (cur.next != None and cur.next != head):
        cur = cur.next

    if cur.next == None:
        return False
    else:
        return True