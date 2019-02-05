def convert_red_black_node_to_str(node):
    if node is None:
        return
    str_buffer = []
    _output_red_black_node(0, node, str_buffer)
    return ''.join(str_buffer)


def _output_red_black_node(indent, node, buffer):
    _output_indent_str(indent, buffer)
    buffer.append(str(node))
    buffer.append('\n')
    if node.left is not None:
        _output_red_black_node(indent + 1, node.left, buffer)
    else:
        _output_indent_str(indent + 1, buffer)
        buffer.append('<NIL,1>\n')
    if node.right is not None:
        _output_red_black_node(indent + 1, node.right, buffer)
    else:
        _output_indent_str(indent + 1, buffer)
        buffer.append('<NIL,1>\n')


def _output_indent_str(indent, buffer):
    for _ in range(indent):
        buffer.append('|  ')
    buffer.append('+--')
