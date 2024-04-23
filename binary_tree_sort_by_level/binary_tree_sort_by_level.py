from collections import deque
'''
A module for sorting tree by levels
'''
class Node:
    '''
    Defines a node of a graph
    '''
    def __init__(self, L, R, n):
        '''
        Initializes a node
        '''
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    '''
    Returns the list with elements from tree sorted by levels.
    '''
    if node is not None:

        res = list()
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            res.append(cur.value)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        return res
    return list()