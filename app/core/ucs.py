from .util import getpath
import heapq

GOAL_STATE = '12345678X'
g_visited = set()
g_front = dict()
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

    return dist

def ucs(root):
    '''implementation of ucs algorithm
    '''
    global GOAL_STATE
    global g_parent
    global g_visited
    global g_front

    class _Node:
        __slots__ = ('puzzle', 'priority')
        def __init__(self, puzzle, priority):
            self.puzzle = puzzle
            self.priority = priority # priority is a tuple: (h,h)

        def __hash__(self):
            return hash(self.puzzle) ^ hash(self.priority)

        def __lt__(self, obj):
            if self.priority != obj.priority:
                return self.priority < obj.priority
            return self.puzzle.state < obj.puzzle.state
    
    if root.solvable() == False:
        #solvable, num_of_nodes, path = ucs(state) in app.py
        return (False, 0, None)

    # using a heap to store best choices
    root_node = _Node(root, (0, 0))
    heap = [root_node]

    while len(heap) != 0 and heap[0].puzzle != GOAL_STATE:
        top = heapq.heappop(heap)

        # mark current node as visited
        g_visited.add(top.puzzle)

        cost = top.priority[0]

        # generate all the possible neighbours
        children = top.puzzle.generate_states()

        for child in children:
            # ignore visited nodes just to improve the efficiency
            if child in g_visited:
                continue

            
            # calculate h and make a node from this child
            h = manhattan_dist(child)
            child_node = _Node(child, (h+cost, h+cost))

            # store on the heap
            # search in the heap and check if the node is in it
            g_parent[child.state] = top.puzzle.state
            prev_cost = g_front.get(child_node.puzzle, None)
            found = False
            if prev_cost is not None:
                if prev_cost > child_node.priority[0]:
                    # find the node in frontier and replace it
                    for idx, node in enumerate(heap):
                        if node.puzzle == child_node.puzzle:
                            found = True
                            del heap[idx]
                            heapq.heappush(heap, child_node)
                            g_front[child_node.puzzle] = child_node.priority[0]
                            break
 
            if not found:
                g_front[child_node.puzzle] = child_node.priority[0]
                heapq.heappush(heap, child_node)
                

    path = getpath(GOAL_STATE, g_parent)
    # (solvable, num of nodes, path)
    return (True, len(g_visited), path)
