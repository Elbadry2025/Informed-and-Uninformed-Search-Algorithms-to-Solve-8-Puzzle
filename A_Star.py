from queue import PriorityQueue
import main
import time

def swap(state, zero, j):
    state_list = list(state)

    state_list[zero], state_list[j] = state_list[j], state_list[zero]

    return ''.join(state_list)


def get_neighbors(state):
    neighbours = []
    zero_index = state.index('0')
    possible_neigbours = [1, -1, 3, -3]

    for i in possible_neigbours:
        temp = zero_index
        temp += i
        if (zero_index % 3 == 2 and i == 1) or (zero_index % 3 == 0 and i == -1) or (zero_index > 5 and i == 3) or (
                zero_index < 3 and i == -3):
            continue
        neighbours.append(swap(state, zero_index, temp))
    return neighbours


def Manhattan_distance(state):
    h = 0
    for i in range(0,len(state), 3):
        for j in range(0,3):
            xval = j
            yval = i/3
            if state[i+j] == '0':
                h = abs(xval - 0) + abs(yval - 0)
            elif state[i+j] == '1':
                h = abs(xval-1) + yval
            elif state[i+j] == '2':
                h = abs(xval-2) + yval
            elif state[i+j] == '3':
                h = abs(xval) + abs(yval-1)
            elif state[i+j] == '4':
                h = abs(xval-1) + abs(yval-1)
            elif state[i+j] == '5':
                h = abs(xval-2) + abs(yval - 1)
            elif state[i+j] == '6':
                h = abs(xval) + abs(yval - 2)
            elif state[i+j] == '7':
                h = abs(xval-1) + abs(yval - 2)
            elif state[i+j] == '8':
                h = abs(xval-2) + abs(yval - 2)
    return h

def A_Star(initial_state, heuristic):
    print("### A Star ###")
    g = 0
    goal = "012345678"
    frontier = PriorityQueue()
    f_frontier = set()
    explored = set()
    Parent_map = {}
    path = []
    frontier.put((0,initial_state))
    f_frontier.add(initial_state)
    # Parent_map.append((initial_state,(initial_state,0+Manhattan_distance(initial_state))))
    Parent_map[initial_state] = (initial_state,g+Manhattan_distance(initial_state))
    while not frontier.empty():
        state = frontier.get()
        f_frontier.remove(state[1])
        explored.add(state[1])

        current_cost = state[0]
        if state[1] == goal:
            print('Success')
            print(len(explored))
            return explored, Parent_map

        neighbours = get_neighbors(state[1])

        for i in neighbours:
            if not (i in explored) and not (i in f_frontier):

                frontier.put((g+Manhattan_distance(i),i))
                f_frontier.add(i)
                g = g + 1
                # print("neighbour entering Priority Queue")
                # Parent_map.append((i,(state,g+Manhattan_distance(i))))
                Parent_map[i] = (state[1],g+Manhattan_distance(i))
            elif (g+Manhattan_distance(i),i) in f_frontier :
                if (g+Manhattan_distance(i)) < Parent_map[i]:
                    Parent_map[i] = (state[1],g+Manhattan_distance(i))
                    frontier.put((g+Manhattan_distance(i),i))
                    f_frontier.add(i)
    return False


grid = "123456780"
start_time = time.time() * 1000
tuple_A_Star = A_Star(grid,True)
end_time = time.time() * 1000
running_time_ms = end_time - start_time
print(f"Your function took {running_time_ms:.2f} milliseconds to run.")

if not tuple_A_Star :
    print("Unsolvable")
else :
    explore = tuple_A_Star[0]
    parent = tuple_A_Star[1]
    state = "012345678"
    n = len(explore)
    print("###  A_Star  ### ")
    print(f"Search Depth && Cost of this solution is : {n}")
    print(f"step {n}")
    n -= 1
    main.printGrid(state)
    while parent[state][0] != grid:
        state = parent[state][0]
        print(f"step {n}")
        n -= 1
        main.printGrid(state)

    print(f"step {n}")
    main.printGrid(grid)