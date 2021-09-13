from .util import getpath 
from heapq import heappush, heappop

GOAL_STATE = '12345678X'
g_visited = set()
g_parent = dict()
g_position = {
    '1': (0, 0),
    '2': (0, 1),
    '3': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '7': (2, 0),
    '8': (2, 1),
}

def ucs(root, limit):
    global GOAL_STATE
    global g_parent
    global g_visited

    class _Node:
        __slots__ = ('puzzle', 'priority')
        def __init__(self, puzzle, priority):
            self.puzzle = puzzle
            self.priority = priority # priority is a tuple: (f, f)

        def __hash__(self):
            return hash(self.puzzle) ^ hash(self.priority)

        def __lt__(self, obj):
            if self.priority != obj.priority:
                return self.priority < obj.priority
            return self.puzzle.state < obj.puzzle.state


    # using a heap to store best choices
    root_node = _Node(root, (0, 0))
    heap = [root_node]

    while len(heap) != 0 and heap[0].puzzle != GOAL_STATE:
        top = heappop(heap)

        if top.priority[0] >= limit:
            return (False, 0, None)

        # mark current node as visited
        g_visited.add(top.puzzle)
        # f(n) = g(n)
        cost = top.priority[0]
        # generate all the possible neighbours
        children = top.puzzle.generate_states()

        for child in children:
            # ignore visited nodes just to improve the efficiency
            if child in g_visited:
                continue

            # set current node as parent of the children
            g_parent[child.state] = top.puzzle.state 
            
            # calculate  f and make a node from this child
            f = (cost + 1) # the child node is on the next level so
                               # the cost is 1 more than the parent cost
            child_node = _Node(child, (f, f))

            # store on the heap
            heappush(heap, child_node)

    path = getpath(GOAL_STATE, g_parent) 

    # (solvable, num of nodes, path)
    return (True, len(g_visited), path)
    
def ils(root):
    global g_parent
    global g_visited
    
    if root.solvable() == False:
        return (False, 0, None)

    limit = 5
    answer = None
    while answer == None:
        g_parent.clear()
        g_visited.clear()
        answer = ucs(root, limit)
        if answer[0] == False:
            answer = None
        limit += 5

    return answer

