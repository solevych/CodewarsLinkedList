class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    data = s.split(' -> ')
    node = None
    for el in reversed(data[:-1]):
        node=Node(int(el), node)
    return node


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


# node = "1 -> 2 -> 123 -> None"
# print(linked_list_from_string(node).data)
# printlink(linked_list_from_string(node))