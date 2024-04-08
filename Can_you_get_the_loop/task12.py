def loop_size(node):    
    slow_ptr = fast_ptr = node
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            length = 1
            fast_ptr = fast_ptr.next
            while slow_ptr != fast_ptr:
                fast_ptr = fast_ptr.next
                length += 1
            return length
    return 0

