from collections import deque
import time


def printGrid(grid):
    formatted_grid = "".join([grid[i:i + 3] + "\n" for i in range(0, len(grid), 3)])

    # Print the formatted grid
    print(formatted_grid, "")

def isgoal(state):
    return state == "012345678"

def swap(state, zero, j):
    state_list = list(state)
    state_list[zero], state_list[j] = state_list[j], state_list[zero]
    return ''.join(state_list)


def get_neighbours(state):
    neighbours = []
    zero_index = state.index('0')
    possible_neigbours = [1, -1, 3, -3]
    
    for i in possible_neigbours:
        temp = zero_index
        temp += i
        if (zero_index%3 == 2 and i == 1) or (zero_index%3 == 0 and i == -1) or (zero_index > 5 and i == 3) or (zero_index < 3 and i == -3):
            continue
        neighbours.append(swap(state, zero_index, temp))
    return neighbours


def DFS(initial_state):
    frontier = deque()
    explored = set()
    front_set = set()
    parent_map = {initial_state: (initial_state, 0)}
    frontier.append((initial_state, 0))
    mx = 0
    front_set.add(initial_state)
    x = 1
    while len(frontier) > 0:
        tuple_frontier = frontier.pop()
        state = tuple_frontier[0]
        cur_cost = tuple_frontier[1]

        front_set.remove(state)
        explored.add(state)
        if isgoal(state):
            return explored, parent_map, mx
        neighbours = get_neighbours(state)

        new_cost = cur_cost + 1
        mx = max(mx, new_cost)
        for i in neighbours:
            if i not in front_set and i not in explored:
                parent_map[i] = (state, new_cost)
                frontier.append((i, new_cost))
                front_set.add(i)

    return False


# grid = "812043765" unsovlable
grid = "123456780"

start_time = time.time() * 1000
tuple_DFS = DFS(grid)
end_time = time.time() * 1000
running_time_ms = end_time - start_time
print(f"Your function took {running_time_ms:.2f} milliseconds to run.")

if not tuple_DFS :
    print("Unsolvable")
else :
    explore = tuple_DFS[0]
    parent = tuple_DFS[1]
    depth = tuple_DFS[2]
    state = "012345678"
    n = parent[state][1]
    print("###  DFS  ### ")
    print(f"Cost of this solution is : {n}")
    print(f"Search Depth : {depth}")
    print(f"step {n}")
    n -= 1
    printGrid(state)
    while parent[state][0] != grid:
        state = parent[state][0]
        print(f"step {n}")
        n -= 1
        printGrid(state)

    print(f"step {n}")
    printGrid(grid)
