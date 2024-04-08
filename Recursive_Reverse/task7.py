class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

def reverse(head):

    if head is None or head.next is None:
        return head

    new_node = reverse(head.next)
    head.next.next = head
    head.next = None

    # new_node = Node()
    # while head is not None:
    #     new_node = Node(head.data, new_node)
    #     head=head.next
    
    return new_node


