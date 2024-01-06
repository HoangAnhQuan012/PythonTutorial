from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("Python Desktop App")

f = ('Times', 14)
var = StringVar()
var.set('male')

language = StringVar()
language.set('English')

countries = []
variable = StringVar()

#  label is Register Form justify center
Label(
    ws,
    text="Register Form",
    font=('Times', 20),
    fg="#000"
).pack(pady=10)

world = open("./Excercises/Week3//Tkinter/Validate/countries.txt", "r", encoding="utf-8")
for country in world:
    country = country.rstrip("\n")
    countries.append(country)

right_frame = Frame(
    ws, bd=2, relief=SOLID, padx=10, pady=10
)

Label(
    right_frame,
    text="Fullname:",
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Email:",
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Gender:",
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Country:",
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Language:",
    font=f
).grid(row=4, column=0, sticky=W, pady=10)


txtFullname = Entry(right_frame, font=f)
txtEmail = Entry(right_frame, font=f)

gender_frame = LabelFrame(right_frame, padx=10, pady=10)
male_rb = Radiobutton(gender_frame, text="Male", variable=var, value='male', font=('Times', 10))
female_rb = Radiobutton(gender_frame, text="Female", variable=var, value='female', font=('Times', 10))

register_country = OptionMenu(right_frame, variable, *countries)
variable.set(countries[0])
register_country.config(width=15, font=('Times', 12))

language_frame = LabelFrame(right_frame, padx=10, pady=10)
English_cb = Checkbutton(language_frame, text="English", variable=language, onvalue="English", offvalue="")
German_cb = Checkbutton(language_frame, text="German", variable=language, onvalue="German", offvalue="")

def Validate_Form():
    error = "Error!"
    if txtFullname.get() == "":
        messagebox.showerror(error, "Fullname doesn't empty")
        txtFullname.focus_set()
        return
    
    if txtEmail.get() == "":
        messagebox.showerror(error, "Email doesn't empty")
        txtEmail.focus_set()
        return
    
    if txtEmail.get().find("@") == -1 or txtEmail.get().find(".") == -1:
        messagebox.showerror(error, "Email doesn't valid")
        txtEmail.focus_set()
        return
    
    if var.get() == "":
        messagebox.showerror(error, "Gender doesn't empty")
        return
    
    if variable.get() == "":
        messagebox.showerror(error, "Country doesn't empty")
        return
    
    if language.get() == "":
        messagebox.showerror(error, "Language doesn't empty")
        return
    
    messagebox.showinfo("Success!", "Register success!")
    
register_btn = Button(right_frame, text="Submit", background="#000", fg="#fff", font=f, relief=SOLID, cursor='hand2', width=20, command=Validate_Form)

txtFullname.grid(
    row=0,
    column=1,
    pady=10,
    padx=20
)

txtEmail.grid(
    row=1,
    column=1,
    pady=10,
    padx=20
)

register_country.grid(
    row=3,
    column=1,
    pady=10,
    padx=20
)

register_btn.grid(
    row=5,
    column=1,
    pady=10,
    padx=20
)

right_frame.pack()

language_frame.grid(row=4, column=1, pady=10, padx=20)
English_cb.pack(expand=True, side=LEFT)
German_cb.pack(expand=True, side=LEFT)

gender_frame.grid(row=2, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)

ws.mainloop()