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


def BFS(initial_state):
    frontier = queue.Queue()
    explored = set()
    front_set = set()
    parent_map = {initial_state: initial_state}
    frontier.put(initial_state)
    front_set.add(initial_state)
    while frontier.qsize() > 0:
        state = frontier.get()
        front_set.remove(state)
        explored.add(state)
        if isgoal(state):
            return parent_map
        neighbors = get_neighbors(state)

        for i in neighbors:
            if i not in front_set and i not in explored:
                parent_map[i] = state
                frontier.put(i)
                front_set.add(i)

    return False


grid = "806547231"
parent = BFS(grid)

if parent:
    x = 0
    state = "012345678"
    printGrid(state)
    while parent[state] != grid:
        x+=1
        printGrid(parent[state])
        state = parent[state]
    printGrid(grid)
    print("Steps = ",x)
else:
    print("Unsolvable")





