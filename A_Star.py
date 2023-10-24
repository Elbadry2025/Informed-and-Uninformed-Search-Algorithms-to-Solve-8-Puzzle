import math
from queue import PriorityQueue
import main
import time


# def printGrid(grid):
#     formatted_grid = "".join([grid[i:i + 3] + "\n" for i in range(0, len(grid), 3)])
#
#     # Print the formatted grid
#     print(formatted_grid, "")
#
#
# def swap(state, zero, j):
#     state_list = list(state)
#
#     state_list[zero], state_list[j] = state_list[j], state_list[zero]
#
#     return ''.join(state_list)
#
#
# def main.get_neighbors(state):
#     neighbors = []
#     zero_index = state.index('0')
#
#     possible_moves = [-1,-3,1,3]
#
#     for move in possible_moves:
#         new_index = zero_index + move
#
#         if (zero_index % 3 == 2 and move == 1) or (zero_index % 3 == 0 and move == -1) or (new_index < 0) or (new_index >= len(state)):
#             continue
#
#         neighbors.append(swap(state, zero_index, new_index))
#
#     return neighbors
#
# def getInvCount(arr):
#     inv_count = 0
#     empty_value = 0
#     for i in range(0, 9):
#         for j in range(i + 1, 9):
#             if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
#                 inv_count += 1
#     return inv_count
#
#
# def isSolvable(puzzle):
#     # Count inversions in given 8 puzzle
#     inv_count = getInvCount([j for sub in puzzle for j in sub])
#
#     # return true if inversion count is even.
#     return (inv_count % 2 == 0)

class ManhattanDistance:
    def distance(self,state):
        h = 0
        for i in range(0,len(state), 3):
            for j in range(0,3):
                xval = j
                yval = i/3

                if state[i+j] == '1':
                    h = h + abs(xval-1) + yval
                elif state[i+j] == '2':
                    h = h + abs(xval-2) + yval
                elif state[i+j] == '3':
                    h = h + abs(xval) + abs(yval-1)
                elif state[i+j] == '4':
                    h = h + abs(xval-1) + abs(yval-1)
                elif state[i+j] == '5':
                    h = h +  abs(xval-2) + abs(yval - 1)
                elif state[i+j] == '6':
                    h = h +  abs(xval) + abs(yval - 2)
                elif state[i+j] == '7':
                    h = h +  abs(xval-1) + abs(yval - 2)
                elif state[i+j] == '8':
                    h = h +  abs(xval-2) + abs(yval - 2)
        return h


class EuclideanDistance:
        def distance(self, state):
            h = 0
            for i in range(0,len(state), 3):
                for j in range(0,3):
                    xval = j
                    yval = i / 3

                    if state[i + j] == '1':
                        h = h + math.sqrt((xval - 1)**2 + yval**2)
                    elif state[i + j] == '2':
                        h = h + math.sqrt((xval - 2)**2 + yval**2)
                    elif state[i + j] == '3':
                        h = h + math.sqrt((xval)**2 + (yval - 1)**2)
                    elif state[i + j] == '4':
                        h = h + math.sqrt((xval - 1)**2 + (yval - 1)**2)
                    elif state[i + j] == '5':
                        h = h + math.sqrt((xval - 2)**2 + (yval - 1)**2)
                    elif state[i + j] == '6':
                        h = h + math.sqrt((xval)**2 + (yval - 2)**2)
                    elif state[i + j] == '7':
                        h = h + math.sqrt((xval - 1)**2 + (yval - 2)**2)
                    elif state[i + j] == '8':
                        h = h + math.sqrt((xval - 2)**2 + (yval - 2)**2)
                return h





def A_Star(initial_state, heuristic):
    g = 0
    if heuristic:
        heur = ManhattanDistance()
    else:
        heur = EuclideanDistance()

    goal = "012345678"
    frontier = PriorityQueue()
    #current_cost = 0
    f_frontier = set()
    explored = set()
    #path = set()
    Parent_map = {initial_state: (initial_state, 0)}
    frontier.put((0+heur.distance(initial_state), initial_state))
    f_frontier.add(initial_state)
    #path.add(initial_state)
    while not (frontier.empty()):
        state = frontier.get()
        f_frontier.remove(state[1])
        explored.add(state[1])
        #path.add(state[1])
        if state[1] == goal:
            # print('Success')
            # print(len(explored))
            return Parent_map, len(explored)

        neighbours = main.get_neighbors(state[1])
        print(f"neigbours of:{state[1]}:\n")
        for j in neighbours:
            print(j+" ",end=""+"\n\n")
        #current_cost += 1
        for i in neighbours:
      #      path.add(i)
      #       print("##############")
      #       main.printGrid(i)

            if not (i in explored) and not (i in f_frontier):
                frontier.put((Parent_map[state[1]][1]+1+heur.distance(i), i))
                f_frontier.add(i)
                Parent_map[i] = (state, Parent_map[state[1]][1]+1)
            elif i in f_frontier:
                if (Parent_map[state[1]][1]+1+ heur.distance(i)) < Parent_map[i][1]:
                    Parent_map[i] = (state[1], Parent_map[state[1]][1]+1)
                    frontier.put((Parent_map[state[1]][1]+1+heur.distance(i), i))
                    f_frontier.add(i)
    return False



grid = "236107845"
heuristic = int(input("Enter 0 for manhattan distance or 1 for Euclidean Distance"))
if heuristic:
    start_time = time.time() * 1000
    tuple_A_Star = A_Star(grid, False)
    end_time = time.time() * 1000
    running_time_ms = end_time - start_time
else:
    start_time = time.time() * 1000
    tuple_A_Star = A_Star(grid, True)
    end_time = time.time() * 1000
    running_time_ms = end_time - start_time
print(f"Your function took {running_time_ms:.2f} milliseconds to run.")

if not tuple_A_Star :
    print("Unsolvable")
else :
    explore = tuple_A_Star[1]
    parent = tuple_A_Star[0]
    state = "012345678"
    #n = tuple_A_Star[2]
    #path = tuple_A_Star[3]

    print("###  A_Star  ### ")
    #print(f"Search Depth && Cost of this solution is : {n}")
    #print(f"step {n}")
    #n -= 1
    main.printGrid(state)
    x = 0
    while parent[state][0][1] != grid:
        x+=1
        state = parent[state][0][1]
        print("step = ",x)
        main.printGrid(state)
    #print("n = ",n)
    print("#explored = ",explore)

    #print(f"step {n}")
    main.printGrid(grid)

