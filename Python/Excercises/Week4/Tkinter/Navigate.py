from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("Python Desktop App")

# set window size
ws.geometry("300x200")
f = ('Times', 14)

Label(
    ws,
    text="This is label widget",
    font=('Times', 20),
    fg="#FF0000"
).pack(pady=10)

btn_widget = Button(
    ws,
    text="This is button widget",
    fg="#0000FF",
    font=f,
)


txtInput = Entry(
    ws,
    font=f,
)

btn_widget.pack(pady=10)
txtInput.pack(pady=10)


def subwindow():
    subwindow = Toplevel(ws)
    subwindow.title("Subwindow")
    
    right_frame = Frame(
        subwindow, bd=2, relief=SOLID, padx=10, pady=10
    )
    
    Label(
        right_frame,
        text="Last Name",
        font=f,
    ).grid(row=0, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="First Name",
        font=f,
    ).grid(row=1, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Job",
        font=f,
    ).grid(row=2, column=0, sticky=W, pady=10)

    Label(
        right_frame,
        text="Country",
        font=f,
    ).grid(row=3, column=0, sticky=W, pady=10)

    txt_last_name = Entry(right_frame, font=f)
    txt_first_name = Entry(right_frame, font=f)
    txt_job = Entry(right_frame, font=f)
    txt_country = Entry(right_frame, font=f)

    btn_show = Button(
        right_frame,
        text="Show",
        font=f,
        width=10,
        command=lambda: messagebox.showinfo(
            "Information",
            f"Last Name: {txt_last_name.get()}\n"
            f"First Name: {txt_first_name.get()}\n"
            f"Job: {txt_job.get()}\n"
            f"Country: {txt_country.get()}"
        )
    )

    btn_quit = Button(
        right_frame,
        text="Quit",
        font=f,
        width=10,
        command=subwindow.destroy
    )

    btn_show.grid(row=4, column=0, sticky=W, pady=10, padx=20)
    btn_quit.grid(row=4, column=1, sticky=W, pady=10, padx=20)

    txt_last_name.grid(row=0, column=1, pady=10, padx=20)
    txt_first_name.grid(row=1, column=1, pady=10, padx=20)
    txt_job.grid(row=2, column=1, pady=10, padx=20)
    txt_country.grid(row=3, column=1, pady=10, padx=20)
    right_frame.pack()

btn_widget.config(command=subwindow)

ws.mainloop()
# Hello
