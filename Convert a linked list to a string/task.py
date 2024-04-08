def stringify(node):
    result=''
    if node is None:
        result+='None'
        return result
    else:
        probe = node
        while probe is not None:
            if probe.next is not None:
                result+=str(probe.data)
                result+= ' -> '
            else:
                result+=str(probe.data)
            probe=probe.next
    result+='-> None'
    return result