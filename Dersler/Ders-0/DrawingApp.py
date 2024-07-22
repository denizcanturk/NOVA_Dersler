import tkinter as tk
from tkinter import ttk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NOVA Drawing App")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{500}x{600}+{100}+{350}")

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.color = tk.StringVar()
        self.color.set("black")

        self.shape = tk.StringVar()
        self.shape.set("circle")

        self.canvas.bind("<B1-Motion>", self.draw)

        self.clear_button = ttk.Button(self.root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack()

        self.color_label = tk.Label(self.root, text="Color:")
        self.color_label.pack()

        self.color_picker = ttk.Combobox(self.root, textvariable=self.color, values=["black", "red", "green", "blue"])
        self.color_picker.pack()
        self.color_picker.bind("<<ComboboxSelected>>", self.update_color)

        self.shape_label = tk.Label(self.root, text="Shape:")
        self.shape_label.pack()

        self.shape_picker = ttk.Combobox(self.root, textvariable=self.shape, values=["circle", "square", "triangle"])
        self.shape_picker.pack()
        self.shape_picker.bind("<<ComboboxSelected>>", self.update_shape)

    def draw(self, event):
        x, y = event.x, event.y
        if self.shape.get() == "circle":
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill=self.color.get(), outline="")
        elif self.shape.get() == "square":
            self.canvas.create_rectangle(x-10, y-10, x+10, y+10, fill=self.color.get(), outline="")
        elif self.shape.get() == "triangle":
            self.canvas.create_polygon(x, y-10, x-10, y+10, x+10, y+10, fill=self.color.get(), outline="")

    def clear_canvas(self):
        self.canvas.delete("all")

    def update_color(self, event):
        self.color.set(self.color_picker.get())

    def update_shape(self, event):
        self.shape.set(self.shape_picker.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
