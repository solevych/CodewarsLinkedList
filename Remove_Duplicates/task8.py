class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if head is None:
        return head
    datas=[head.data]
    probe = head
    while probe is not None and probe.next is not None:
        print(probe.data)
        if probe.next.data not in datas:
            datas.append(probe.next.data)
            probe=probe.next
        else:
            probe.next=probe.next.next
            # probe=probe.next
    return head


# node = Node(1, Node(1, Node(2, Node(3, Node(2, None)))))

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
# printlink(remove_duplicates(node))