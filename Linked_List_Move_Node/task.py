class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    front_node=Node(source.data)
    front_node.next = dest
    source=source.next
    dest = front_node
    return Context(source, dest)