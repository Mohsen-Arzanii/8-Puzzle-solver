from heapq import heappush, heappop
from .util import getpath 

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

def manhattan_dist(puzzle):
    '''calculate heuristic for a given state
       input: Puzzle
       return: manhattan_distance: int
    '''
    global g_position
    # we store each state in a flat string so the
    # good idea is to calculate row and col using div and mod oprators
    # and compare each position with their actual mapping
    dist = 0
    for indx, cell in enumerate(puzzle.state):
        # ignore empty space
        if cell == 'X':
            continue

        row = indx // 3
        col = indx % 3
        
        # actual row, column; treat all non-digits like X
        acrow, accol = g_position.get(cell, (2, 2))
        dist += abs(row - acrow) + abs(col - accol)
        d = abs(row - acrow) + abs(col - accol)

    return dist

def astar(root):
    '''implemention of astar algorithm
    '''
    global GOAL_STATE
    global g_parent
    global g_visited

    class _Node:
        __slots__ = ('puzzle', 'priority')
        def __init__(self, puzzle, priority):
            self.puzzle = puzzle
            self.priority = priority # priority is a tuple: (f, h)

        def __hash__(self):
            return hash(self.puzzle) ^ hash(self.priority)

        def __lt__(self, obj):
            if self.priority != obj.priority:
                return self.priority < obj.priority
            return self.puzzle.state < obj.puzzle.state


    # first of all check if the state is solvable at least
    if root.solvable() == False:
        return (False, 0, None)

    # so reset parent and visited
    g_parent.clear()
    g_visited.clear()

    # using a max-heap to store best choices
    root_node = _Node(root, (0, 0))
    heap = [root_node]

    while len(heap) != 0 and heap[0].puzzle != GOAL_STATE:
        top = heappop(heap)

        # mark current node as visited
        g_visited.add(top.puzzle)

        # cost of the node is f - h
        # we will use it later in the child nodes to calculate f for children
        cost = top.priority[0] - top.priority[1]
        # generate all the possible neighbours
        children = top.puzzle.generate_states()

        for child in children:
            # ignore visited nodes just to improve the efficiency
            if child in g_visited:
                continue

            # set current node as parent of the children
            g_parent[child.state] = top.puzzle.state 
            
            # calculate h and f and make a node from this child
            h = manhattan_dist(child)
            f = h + (cost + 1) # the child node is on the next level so
                               # the cost is 1 more than the parent cost
            child_node = _Node(child, (f, h))

            # store on the heap
            heappush(heap, child_node)

    path = getpath(GOAL_STATE, g_parent) 

    # (solvable, num of nodes, path)
    return (True, len(g_visited), path)

