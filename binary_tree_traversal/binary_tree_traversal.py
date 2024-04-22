'''
The module represents a functions for different travestals
'''
def pre_order(node):
    '''
    Pre-order travestal
    '''
    if node is not None:
        result = [node.data]
        result.extend(pre_order(node.left))
        result.extend(pre_order(node.right))
        return result
    return list()

def in_order(node):
    '''
    In-order traversal
    '''
    if node is not None:
        result = in_order(node.left)
        result.append(node.data)
        result.extend(in_order(node.right))
        return result
    return list()

def post_order(node):
    '''
    Post-order traversal
    '''
    if node is not None:
        result = post_order(node.left)
        result.extend(post_order(node.right))
        result.append(node.data)
        return result
    return list()