from collections import deque
import main

def DFS(initial_state):
    frontier = deque()
    explored = set()
    parent_map = {initial_state: (initial_state, 0)}
    frontier.append(initial_state)

    x = 1
    while len(frontier) > 0:
        state = frontier.pop()

        explored.add(state)
        if main.isgoal(state):
            return parent_map,len(explored)
        neighbours = main.get_neighbors(state)

        for i in reversed(neighbours):
            if i not in parent_map and i not in explored:
                parent_map[i] = (state, parent_map[state][1]+1)
                frontier.append(i)

    return False

#