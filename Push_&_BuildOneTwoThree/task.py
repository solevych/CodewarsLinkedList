'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

# from preloaded import Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    node = None
    for el in [3, 2, 1]:
        node_prev = node
        node = Node(el)
        node.next = node_prev
    return node
