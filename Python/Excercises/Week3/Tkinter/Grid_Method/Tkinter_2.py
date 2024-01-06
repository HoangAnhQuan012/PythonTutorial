import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# root window
root = tk.Tk()
root.geometry("240x100")
root.title("Login")
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

def login():
    if username_entry.get() == "user" and password_entry.get() == "pass":
        messagebox.showinfo(title="Login", message="Login Successful")
    else:
        messagebox.showerror(title="Login", message="Login Failed")

# login button
login_button = ttk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

root.mainloop()