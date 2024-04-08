class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def reverse(head):

    if head is None or head.next is None:
        return head
    new_node = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_node

def split_node(probe):
    count=0
    node = None
    while probe is not None:
        count+=1
        node=Node(probe.data, node)
        if probe.next:
            probe=probe.next.next
        else:
            probe=None
    return (node, count) 
 
def alternating_split(head):
    if head is None or head.next is None:
        raise TypeError
    head = reverse(head)


    probe1, count1=split_node(head)
    probe2, count2=split_node(head.next)
    # printlink(head.next)

    return Context(probe1, probe2) if count1 != count2 else Context(probe2, probe1)


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
# node=Node(1, Node(2, Node(1, Node(4,  Node(5, None)))))
# printlink(node)
# # alternating_split(node)
# printlink(alternating_split(node).first)
# # printlink(alternating_split(node).second)