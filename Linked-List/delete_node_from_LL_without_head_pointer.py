# Note: No head reference is given to you.
# It is guaranteed that the node to be deleted is not the last node;

def removeNode(node):

    # TC: O(1)
    # SC: O(1)

    if node == None:
        return

    # copy next node value
    node.val = node.next.val

    # point to next of next node
    node.next = node.next.next
