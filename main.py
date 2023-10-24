import queue



def printGrid(grid):
    for i in range(9):
        print(grid[i],end="")
        if((i+1) % 3 == 0):
            print("\n")
    print("\n")


def isgoal(state):
    return state == "012345678"

def swap(state, zero, j):
    state_list = list(state)

    state_list[zero], state_list[j] = state_list[j], state_list[zero]

    return ''.join(state_list)


def get_neighbors(state):
    neighbors = []
    zero_index = state.index('0')

    possible_moves = [-1,-3,1,3]

    for move in possible_moves:
        new_index = zero_index + move

        if (zero_index % 3 == 2 and move == 1) or (zero_index % 3 == 0 and move == -1) or (new_index < 0) or (new_index >= len(state)):
            continue

        neighbors.append(swap(state, zero_index, new_index))

    return neighbors
















