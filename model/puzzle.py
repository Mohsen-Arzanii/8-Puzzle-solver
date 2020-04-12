class Puzzle:
    __slots__ = ('state', )
    def __init__(self, state='12345678X'):
        self.state = state

    def __eq__(self, puzzle2):
        return self.state == puzzle2.state

    def __repr__(self):
        return self.state

    def __hash__(self):
        return hash(self.state)

    def generate_states(self):
        '''generate possible states according to current state
        '''
        # find empty space
        index = self.state.find('X')
        
        # bad representation (8 puzzle len must be 9)
        if len(self.state) != 9:
            raise ValueError('bad representation of puzzle state. len must be 9')

        # bad state representation (empty space not found)
        if index == -1:
            raise ValueError('bad representation of puzzle state. X not found') 

        # generate, validate and store states
        possible_states = []
        right, left, down, up = (index + 1, index - 1, index + 3, index - 3)

        if  self._same_row(index, left) and self._correct_index(left):
            _new_state = self._swap_cells(index, left)
            possible_states.append(Puzzle(_new_state))
        
        if self._same_row(index, right) and self._correct_index(right):
            _new_state = self._swap_cells(index, right)
            possible_states.append(Puzzle(right))

        if self._correct_index(up):
            _new_state = self._swap_cells(index, up)
            possible_states.append(Puzzle(_new_state))

        if self._correct_index(down):
            _new_state = self._swap_cells(index, down)
            possible_states.append(Puzzle(_new_state))

        return possible_states

    def _same_row(self, index1, index2):
        '''check if two items are in same row
        '''
        return True if (index1 // 3 == index2 // 3) else False

    def _correct_index(self, index):
        '''check if the index is vaid
        '''
        return True if (0 <= index < 9) else False

    def _swap_cells(self, index1, index2):
        '''swap two cells in the state
        '''
        _state = list(self.state)
        _state[index1], _state[index2] = _state[index2], _state[index1]
        return ''.join(_state)
            
