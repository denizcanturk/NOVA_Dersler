import tkinter as tk

class RollingText(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=600, height=100, bg='white')
        self.canvas.pack()

        self.text = self.canvas.create_text(600, 50, text="------PYTHON SINIFINA BEKLERİZ! :) - NOVA ACADEMY------", font=("Helvetica", 20), fill="black")

        self.roll_text()

    def roll_text(self):
        self.canvas.move(self.text, -1, 0)  # Move the text to the left by 1 pixel
        x, _ = self.canvas.coords(self.text)  # Get the current coordinates of the text
        if x < -200:  # If the text has moved completely out of the canvas
            self.canvas.coords(self.text, 600, 50)  # Reset the text to the right side of the canvas
        self.after(30, self.roll_text)  # Repeat the rolling every 30 milliseconds

if __name__ == "__main__":
    root = tk.Tk()
    root.title("NOVA ACADEMY")
    # Set window size and position
    window_width = 600
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2  # Center the window horizontally
    y_position = (screen_height - window_height) // 4 + (screen_height - window_height) // 2 + 100 # Center the window vertically
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    app = RollingText(master=root)
    app.pack()
    root.mainloop()
