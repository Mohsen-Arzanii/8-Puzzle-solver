from .util import getpath 

GOAL_STATE = '12345678X'
g_visited = set()
g_parent = dict()

def dfs_with_limit(node, limit):
    '''implemention of dfs algorithm with applying deep limit
    '''
    global GOAL_STATE
    global g_visited
    global g_parent

    # mark the node as visited
    g_visited.add(node)
    # found the answer 
    if node.state == GOAL_STATE:
        return node

    if limit == -1:
        return None

    children = node.generate_states()
    for child in children:
        # ignore visited nodes
        if child in g_visited:
            continue

        # set parent with current node, parent is useful to find the path
        g_parent[child.state] = node.state

        result = dfs_with_limit(child, limit - 1)
        # found the answer
        if result != None:
            return result

    return None
    
def ids(root):
    '''implemention of iterating deeping dfs
    more details in: https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search
    input:  root: Puzzle
    return: tuple -> (is_solvable: bool, list_of_states: list<str>)
            if is_solvable is False, we don't care about the second item
    '''
    global g_parent
    global g_visited
    
    if root.solvable() == False:
        return (False, None)

    limit = 5
    answer = None
    while answer == None:
        g_parent.clear()
        g_visited.clear()
        answer = dfs_with_limit(root, limit)
        limit += 5
    
    if answer == None:
        return (False, None)
    
    path = getpath(GOAL_STATE, g_parent)
    return (True, path)

