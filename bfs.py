import main
import queue


def BFS(initial_state):
    frontier = queue.Queue()
    explored = set()

    parent_map = {initial_state: (initial_state, 0)}
    frontier.put(initial_state)
    maxDepth = 0
    while frontier.qsize() > 0:
        state = frontier.get()
        explored.add(state)
        if main.isgoal(state):
            return parent_map, len(explored), maxDepth
        neighbors = main.get_neighbors(state)

        for i in neighbors:
            if i not in parent_map and i not in explored:
                maxDepth = max(maxDepth, parent_map[state][1] + 1)
                parent_map[i] = (state, parent_map[state][1] + 1)
                frontier.put(i)

    return False

