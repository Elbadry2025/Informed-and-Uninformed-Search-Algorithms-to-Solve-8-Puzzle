from collections import deque
import main

def DFS(initial_state):
    frontier = deque()
    explored = set()
    parent_map = {initial_state: (initial_state, 0)}
    frontier.append(initial_state)
    maxDepth = 0
    while len(frontier) > 0:
        state = frontier.pop()

        explored.add(state)
        if main.isgoal(state):
            return parent_map,len(explored),maxDepth
        neighbours = main.get_neighbors(state)

        for i in reversed(neighbours):
            if i not in parent_map and i not in explored:
                maxDepth = max(maxDepth,parent_map[state][1]+1)
                parent_map[i] = (state, parent_map[state][1]+1)
                frontier.append(i)

    return False

#