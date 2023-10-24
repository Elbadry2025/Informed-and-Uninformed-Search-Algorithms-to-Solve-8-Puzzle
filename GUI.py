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

def read_text_boxes():
    values = [textBoxes[i].get() for i in range(9)]
    values_string = ''.join(values)
    return values_string

window = tk.Tk()
window.title("8 Puzzle Game")
window.geometry("900x900")
window.config(bg="cyan")
# Create a frame to hold the text boxes
frame = tk.Frame(window)
frame.pack(pady=10)

label = tk.Label(window, text="Fill the grid and Choose the searching method", font=("Arial", 12), bg="cyan")
label.pack()

# Create the 3x3 grid of text boxes
textBoxes = []
for i in range(9):
    textBox = tk.Entry(frame, width=7, borderwidth= 1, relief= "solid", font=("Arial", 24))
    textBox.insert(0, f"{i}")
    textBoxes.append(textBox)
    textBox.grid(row=i // 3, column=i % 3)

method = tk.StringVar()
method.set("Choose search method")  # Set the default method
dropdown = tk.OptionMenu(window, method, "BFS", "DFS", "A* Euclidean", "A* Manhattan")
dropdown.pack(pady=25)

solve_button = tk.Button(window, text="Solve", font=("Arial", 24))
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
        explore = result[1]
        parent = result[0]
        state = "012345678"
        n = parent[state][1]
        maxDepth = 0
        for key in parent:
            if parent[key][1] > maxDepth:
                maxDepth = parent[key][1]

        label = tk.Label(window, text=f"Cost of this solution is : {n}\n"
                                      f"Depth of the search is : {maxDepth}\n"
                                      f"Number of explored nodes: {explore}", font=("Arial", 15)
                         ,bg= "white")
        label.pack()

        ans_frame = tk.Frame(window, borderwidth=2, relief="solid", bg="red")
        ans_frame.pack(pady=10)
        answer = []
        for i in range(9):
            label = tk.Label(ans_frame, text=f"{grid[i]}",width=4, height=2, font=("Arial", 25)
                             , borderwidth=4 , relief="solid")
            answer.append(label)
            label.grid(row=i // 3, column=i % 3)

        stack = deque()
        stack.append(state)
        stack2 = deque()
        while state != grid:
            state = parent[state][0]
            #print(state)
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
