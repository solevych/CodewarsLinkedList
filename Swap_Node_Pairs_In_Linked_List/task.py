# from preloaded import Node

class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    probe = Node()
    probe.next = head
    prev = probe
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return probe.next
    # curNode = Node(head)
    # head = head.next

    # while curNode.next is not None and curNode.next.next is not None:
    #     prevNode = curNode.next.next.next
    #     curNode.next.next.next = curNode.next
    #     curNode.next = curNode.next.next
    #     curNode.next.next.next = prevNode
    
    # return head


# node = Node(1, Node(9, Node(3, Node(11, None))))

# def printlink(head):
#     if head is None:
#         print(None)
#     else:
#         probe = head
#         while probe is not None:
#             if probe.next is not None:
#                 print(probe.data, end = '–>')
#             else:
#                 print(probe.data)
#             probe = probe.next
# printlink(node)
# printlink(swap_pairs(node))