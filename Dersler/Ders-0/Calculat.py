import tkinter as tk

def button_click(symbol):
    current = display.get()
    if symbol == 'C':
        display.delete(0, tk.END)
    elif symbol == '=':
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, symbol)

root = tk.Tk()
root.title("Simple Calculator")

# Set window size and position
window_width = 250
window_height = 230
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = 100 #(screen_width - window_width) // 2  # Center the window horizontally
y_position = 50 #(screen_height - window_height) // 2  # Center the window vertically
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_index = 1
col_index = 0

for button_symbol in buttons:
    tk.Button(root, text=button_symbol, padx=20, pady=10, command=lambda symbol=button_symbol: button_click(symbol)).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

root.mainloop()
