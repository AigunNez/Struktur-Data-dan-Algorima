import tkinter as tk
from tkinter import messagebox
import time

def linear_search_visual(arr, target):
    canvas.delete("all")
    bar_width = 40
    canvas_height = 100
    for i, val in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - 40
        x1 = x0 + bar_width - 5
        y1 = canvas_height
        color = "gray"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, tags=f"rect{i}")
        canvas.create_text(x0 + 15, y1 + 10, text=str(val), tags=f"text{i}")
        
    root.update()
    
    for i in range(len(arr)):
        canvas.itemconfig(f"rect{i}", fill="blue")
        root.update()
        time.sleep(0.5)
        
        if arr[i] == target:
            canvas.itemconfig(f"rect{i}", fill="green")
            root.update()
            return i, i +1
        
        
        canvas.itemconfig(f"rect{i}", fill="red")
        root.update()
        
    return None, len(arr)

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return None

def on_search():
    array = list(map(int, entry_array.get().split(',')))
    target = int(entry_target.get())
    result = linear_search_visual(array, target)
    
    if result is not None:
        result_var.set(f"Element found at index: {result}")
    else : 
        result_var.set("Element not found")

root = tk.Tk()
root.title("Linear Search")

tk.Label(root, text="Enter a list of numbers (comma separated):").pack()
entry_array = tk.Entry(root)
entry_array.pack()

tk.Label(root, text="Enter the number to search for:").pack()
entry_target = tk.Entry(root)
entry_target.pack()

tk.Button(root, text="Cari", command=on_search).pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, fg="blue").pack()

canvas = tk.Canvas(root, width=800, height=130, bg="white")
canvas.pack(pady=10)

root.mainloop()