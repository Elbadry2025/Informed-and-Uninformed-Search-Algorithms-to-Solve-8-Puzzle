from collections import deque
import time

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

loopCounter = 1
def DFS(initial_state):
    global loopCounter
    frontier = deque()
    explored = set()
    front_set = set()
    parent_map = {initial_state: initial_state}
    frontier.append(initial_state)
    front_set.add(initial_state)
    while len(frontier) > 0:
        state = frontier.pop()
        front_set.remove(state)
        explored.add(state)
        if isgoal(state):
            loopCounter +=1
            return parent_map
        neighbours = get_neighbours(state)

        for i in neighbours:
            if i not in front_set and i not in explored:
                parent_map[i] = state
                frontier.append(i)
                front_set.add(i)
        loopCounter += 1

    return False


# grid = "812043765" unsovlable
grid = "012345687"
current_time_ms = int(round(time.time() * 1000))
parent = DFS(grid)
updated_time_ms = int(round(time.time() * 1000))
elapsed_time_ms = updated_time_ms - current_time_ms

if(parent):
    state = "012345678"
    print(state)
    while parent[state] != grid:
        print(parent[state])
        state = parent[state]
    print(grid)
else:
    print("Unsolvable")


print("Elapsed time in milliseconds:", elapsed_time_ms)
print(loopCounter)
