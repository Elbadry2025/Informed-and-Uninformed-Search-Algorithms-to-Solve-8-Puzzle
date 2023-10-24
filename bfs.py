import main
import queue


def BFS(initial_state):
    frontier = queue.Queue()
    explored = set()

    # front_set = set()
    parent_map = {initial_state: (initial_state, 0)}
    frontier.put(initial_state)
    # front_set.add(initial_state)
    while frontier.qsize() > 0:
        state = frontier.get()
        # front_set.remove(state)
        explored.add(state)
        if main.isgoal(state):
            return parent_map, len(explored)
        neighbors = main.get_neighbors(state)

        for i in neighbors:
            if i not in parent_map and i not in explored:
                parent_map[i] = (state, parent_map[state][1] + 1)
                frontier.put(i)
                # front_set.add(i)

    return False, False

# grid = "806547231"
# parent,n = BFS(grid)
#
# print(n)
#
# if parent:
#     x = 0
#     state = "012345678"
#     main.printGrid(state)
#     while parent[state][0] != grid:
#         x+=1
#         main.printGrid(parent[state][0])
#         print("depth = ",parent[state][1])
#         state = parent[state][0]
#     main.printGrid(grid)
#     print("Steps = ",x)
# else:
#     print("Unsolvable")
