from collections import deque
import time


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

    possible_moves = [3,1,-3,-1]

    for move in possible_moves:
        new_index = zero_index + move

        if (zero_index % 3 == 2 and move == 1) or (zero_index % 3 == 0 and move == -1) or (new_index < 0) or (new_index >= len(state)):
            continue

        neighbors.append(swap(state, zero_index, new_index))

    return neighbors


def DFS(initial_state):
    frontier = deque()
    explored = set()
    #front_set = set()
    parent_map = {initial_state: (initial_state, 0)}
    frontier.append(initial_state)
    #mx = 0
    #front_set.add(initial_state)
    x = 1
    while len(frontier) > 0:
        state = frontier.pop()
       # state = tuple_frontier[0]
       # cur_cost = tuple_frontier[1]

        #front_set.remove(state)
        explored.add(state)
        if isgoal(state):
            return parent_map,len(explored)
        neighbours = get_neighbors(state)

        #new_cost = cur_cost + 1
        #mx = max(mx, new_cost)
        for i in neighbours:
            if i not in parent_map and i not in explored:
                parent_map[i] = (state, parent_map[state][1]+1)
                frontier.append(i)
                #front_set.add(i)

    return False


grid = "806547231"
parent,n = DFS(grid)

#print(n)

if parent:
    x = 0
    state = "012345678"
    printGrid(state)
    while parent[state][0] != grid:
        x+=1
        printGrid(parent[state][0])
        print("depth = ",parent[state][1])
        state = parent[state][0]
    printGrid(grid)
    print("Steps = ",x)
else:
    print("Unsolvable")
