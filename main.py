import queue


def isgoal(state):
    return state == "012345678"


list_mid_index = [3, 1, 5, 7]
list_upperLeft_index = [1, 3]
list_upperRight_index = [1, 5]
list_bottomLeft_index = [3, 7]
list_bottomRight_index = [7, 5]
list_midTop_index = [0, 2, 4]
list_midLeft_index = [0, 4, 6]
list_midRight_index = [4, 2, 8]
list_midBottom_index = [6, 4, 8]


def swap(state, zero, j):
    # Convert the string to a list to perform the swap
    state_list = list(state)

    # Perform the swap
    state_list[zero], state_list[j] = state_list[j], state_list[zero]

    # Convert the list back to a string
    return ''.join(state_list)


def get_neighbors(state):
    neighbors = []
    zero_index = state.index('0')
    if zero_index == 4:
        for i in list_mid_index:
            neighbors.append(swap(state, zero_index, i))
    elif zero_index == 0:
        for i in list_upperLeft_index:
            neighbors.append(swap(state, zero_index, i))
    elif zero_index == 2:
        for i in list_upperRight_index:
            neighbors.append(swap(state, zero_index, i))
    elif zero_index == 6:
        for i in list_bottomLeft_index:
            neighbors.append(swap(state, zero_index, i))
    elif zero_index == 8:
        for i in list_bottomRight_index:
            neighbors.append(swap(state, zero_index, i))
    elif zero_index == 1:
        for i in list_midTop_index:
            neighbors.append(swap(state, zero_index, i))
    elif zero_index == 3:
        for i in list_midLeft_index:
            neighbors.append(swap(state, zero_index, i))
    elif zero_index == 5:
        for i in list_midRight_index:
            neighbors.append(swap(state, zero_index, i))
    elif zero_index == 7:
        for i in list_midBottom_index:
            neighbors.append(swap(state, zero_index, i))
    return neighbors


def BFS(initial_state):
    #print(initial_state)
    frontier = queue.Queue()
    explored = set()
    front_set = set()
    parent_map = {initial_state: initial_state}
    frontier.put(initial_state)
    front_set.add(initial_state)
    x = 1
    while frontier.qsize() > 0:
        #print("size = ",frontier.qsize())
        #print(x)
        #x+=1
        state = frontier.get()
        front_set.remove(state)
        #print(state)
        explored.add(state)
        if isgoal(state):
            return parent_map
        neighbors = get_neighbors(state)

        for i in neighbors:
            if i not in front_set and i not in explored:
                #print("Stucked in 85")
                parent_map[i] = state
                frontier.put(i)
                front_set.add(i)

    return False


grid = "812043765"
parent = BFS(grid)


if(parent):
    state = "012345678"
    print(state)
    while parent[state] != grid:
        print(parent[state])
        state = parent[state]
    print(grid)
else:
    print("Unsolvable")

#print(BFS(grid))
