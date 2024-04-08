# from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    count=0
    if index>=0 and isinstance(node, Node):
        while node is not None and count<=index:
            if index==count:
                return Node(node.data)
            count+=1
            node=node.next
    raise TypeError