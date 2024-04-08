""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printlink(head):
    if head is None:
        print(None)
    else:
        probe = head
        while probe is not None:
            if probe.next is not None:
                print(probe.data, end='->')
            else:
                print(probe.data)
            probe=probe.next


def sorted_insert(head, data):
    if head is None:
        head = Node(data)
        return head
    if head.data > data:
            prev_head=head
            head = Node(data)
            head.next=prev_head
            return head
    curNode = head
    while curNode.next is not None and curNode.next.data < data:
        curNode = curNode.next
    curNode.next = Node(data, curNode.next)
    return head



    # if head is None:
    #     head = Node(data)
            # return head
    # while head is not None:
    #     if head.data > data:
    #         prev_head=head
    #         head = Node(data)
    #         head.next=prev_head
    #         return head
    #     elif head.data < data and (head.next is None or head.next.data > data):
    #         next_prev= head.next
    #         head.next = Node(data)
    #         head.next.next = next_prev
    #         return head
    #     head=head.next

