import tkinter as tk

win = tk.Tk()
win.title("Python GUI")
win.geometry("300x200")

for i in range(5):
    for j in range(3):
        frame = tk.Frame(
            master=win,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

win.mainloop()