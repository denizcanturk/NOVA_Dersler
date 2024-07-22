import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to update the plot based on user input
def update_plot():
    x = float(entry_x.get())
    y = float(entry_y.get())
    ax.scatter(x, y, color='red')
    canvas.draw()

# Create the main application window
root = tk.Tk()
root.title("Data Visualization Demo")

# Create a frame for the GUI elements
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create entry fields for data input
label_x = ttk.Label(frame, text="X:")
label_x.grid(row=0, column=0, sticky=tk.W)
entry_x = ttk.Entry(frame)
entry_x.grid(row=0, column=1)

label_y = ttk.Label(frame, text="Y:")
label_y.grid(row=1, column=0, sticky=tk.W)
entry_y = ttk.Entry(frame)
entry_y.grid(row=1, column=1)

# Create a button to update the plot
update_button = ttk.Button(frame, text="Update Plot", command=update_plot)
update_button.grid(row=2, columnspan=2)

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Create a canvas to display the plot within the GUI
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=0)

# Start the GUI event loop
root.mainloop()
