import dfs
import bfs
import A_Star
import tkinter as tk
import time
from collections import deque

def printNext(stack, stack2, answer):
    if stack:
        state = stack.pop()
        stack2.append(state)
        if stack:
            for i in range(9):
                answer[i].config(text=stack[-1][i])
def printBack(stack, stack2, answer):
    if not stack:
        stack.append(stack2.pop())
    if stack2:
        state = stack2.pop()
        stack.append(state)
        for i in range(9):
            answer[i].config(text=state[i])

def isgoal(state):
    return state == "012345678"

def swap(state, zero, j):
    state_list = list(state)

    state_list[zero], state_list[j] = state_list[j], state_list[zero]

    return ''.join(state_list)


def get_neighbors(state):
    neighbors = []
    zero_index = state.index('0')

    possible_moves = [-1,-3,1,3]

    for move in possible_moves:
        new_index = zero_index + move

        if (zero_index % 3 == 2 and move == 1) or (zero_index % 3 == 0 and move == -1) or (new_index < 0) or (new_index >= len(state)):
            continue

        neighbors.append(swap(state, zero_index, new_index))

    return neighbors






def read_text_boxes():
    values = [textBoxes[i].get() for i in range(9)]
    values_string = ''.join(values)
    return values_string

window = tk.Tk()
window.title("8 Puzzle Game")
window.geometry("900x700")
window.config(bg="cyan")
# Create a frame to hold the text boxes
frame = tk.Frame(window)
frame.pack(pady=10)

label = tk.Label(window, text="Fill the grid and Choose the searching method", font=("Arial", 12), bg="cyan")
label.pack()

# Create the 3x3 grid of text boxes
textBoxes = []
for i in range(9):
    textBox = tk.Entry(frame, width=5, borderwidth= 1, relief= "solid", font=("Arial", 12))
    textBox.insert(0, f"{i}")
    textBoxes.append(textBox)
    textBox.grid(row=i // 3, column=i % 3)

method = tk.StringVar()
method.set("Choose search method")  # Set the default method
dropdown = tk.OptionMenu(window, method, "BFS", "DFS", "A* Euclidean", "A* Manhattan")
dropdown.pack(pady=25)

solve_button = tk.Button(window, text="Solve", font=("Arial", 12))
solve_button.pack(pady=20)

def solve():
    grid = read_text_boxes()
    start_time = time.time() * 1000
    if method.get() == "BFS":
        result = bfs.BFS(grid)
    elif method.get() == "DFS":
        result = dfs.DFS(grid)
    elif method.get() == "A* Euclidean":
        result = A_Star.A_Star(grid, True)
    else:
        result = A_Star.A_Star(grid, False)
    end_time = time.time() * 1000

    if not result:
        print("Unsolvable")
    else:
        print("Time taken:", end_time - start_time, "ms")
        explore = result[0]
        parent = result[1]
        state = "012345678"
        n = parent[state][1]
        label = tk.Label(window, text=f"Search Depth && Cost of this solution is : {n}\n"
                                      f"Number of explored nodes: {len(explore)}", font=("Arial", 15)
                         ,bg= "white")
        label.pack()

        ans_frame = tk.Frame(window, borderwidth=2, relief="solid", bg="red")
        ans_frame.pack(pady=10)
        answer = []
        for i in range(9):
            label = tk.Label(ans_frame, text=f"{grid[i]}",width=4, height=2, font=("Arial", 15)
                             , borderwidth=4 , relief="solid")
            answer.append(label)
            label.grid(row=i // 3, column=i % 3)

        stack = deque()
        stack.append(state)
        stack2 = deque()
        while state != grid:
            state = parent[state][0]
            stack.append(state)
        for i in range(9):
            answer[i].config(text=grid[i])
        button1 = tk.Button(window, text="Next", font=("Arial", 12))
        button1.pack(pady = 10)
        button2 = tk.Button(window, text ="Back", font=("Arial", 12))
        button2.pack()

        button1.config(command=lambda: printNext(stack, stack2, answer))
        button2.config(command=lambda: printBack(stack, stack2, answer))

solve_button.config(command=solve)
window.mainloop()











