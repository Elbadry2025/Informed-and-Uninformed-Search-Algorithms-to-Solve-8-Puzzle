import queue
import tkinter as tk
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


def get_neighbors(state):
    neighbors = []
    zero_index = state.index('0')
    possible_moves = [-3, 3, -1, 1]

    for move in possible_moves:
        new_index = zero_index + move

        if 0 <= new_index < len(state):
            neighbors.append(swap(state, zero_index, new_index))

    return neighbors


def BFS(initial_state):
    frontier = queue.Queue()
    explored = set()
    front_set = set()
    parent_map = {initial_state: initial_state}
    frontier.put((initial_state, 0))
    front_set.add(initial_state)
    while frontier.qsize() > 0:
        pair_value = frontier.get()
        state = pair_value[0]
        cur_cost = pair_value[1]
        front_set.remove(state)
        explored.add(state)
        if isgoal(state):
            return explored, parent_map
        neighbors = get_neighbors(state)

        for i in neighbors:
            if i not in front_set and i not in explored:
                parent_map[i] = (state, cur_cost+1)
                frontier.put((i, cur_cost+1))
                front_set.add(i)

    return False



grid = "123045678"
start_time = time.time() * 1000
tuple_BFS = BFS(grid)
end_time = time.time() * 1000
running_time_ms = end_time - start_time
print(f"Your function took {running_time_ms:.2f} milliseconds to run.")

if not tuple_BFS :
    print("Unsolvable")
else :
    explore = tuple_BFS[0]
    parent = tuple_BFS[1]
    state = "012345678"
    n = parent[state][1]
    print("###  BFS  ### ")
    print(f"Search Depth && Cost of this solution is : {n}")
    print(f"step {n}")
    n -= 1
    printGrid(state)
    while parent[state][0] != grid:
        state = parent[state][0]
        print(f"step {n}")
        n -= 1
        printGrid(state)
        state = parent[state][0]

    print(f"step {n}")
    printGrid(grid)


