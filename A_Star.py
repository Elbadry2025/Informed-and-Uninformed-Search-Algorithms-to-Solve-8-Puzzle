import math
from queue import PriorityQueue
import main

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
    f_frontier = set()
    explored = set()
    Parent_map = {initial_state: (initial_state, 0)}
    frontier.put((0+heur.distance(initial_state), initial_state))
    f_frontier.add(initial_state)
    maxDepth = 0
    while frontier.qsize() > 0:
        state = frontier.get()
        if state[1] in explored:
            continue
        f_frontier.remove(state[1])

        explored.add(state[1])
        if state[1] == goal:
            return Parent_map, len(explored), maxDepth

        neighbours = main.get_neighbors(state[1])

        for i in neighbours:
            if not (i in explored) and not (i in f_frontier):
                maxDepth = max(maxDepth,Parent_map[state[1]][1]+1)
                frontier.put((Parent_map[state[1]][1]+1+heur.distance(i), i))
                f_frontier.add(i)
                Parent_map[i] = (state[1], Parent_map[state[1]][1]+1)
            elif i in f_frontier:
                if (Parent_map[state[1]][1]+1) < Parent_map[i][1]:
                    Parent_map[i] = (state[1], Parent_map[state[1]][1]+1)
                    frontier.put((Parent_map[state[1]][1]+1+heur.distance(i), i))
                    f_frontier.add(i)

    return False

