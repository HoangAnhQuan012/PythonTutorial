from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("Resgister Form")

f = ('Times', 14)

dob_var = StringVar()
gender_var = StringVar()
gender_var.set('male')
sc_var = StringVar()

ListDate = [
    "01/12/2023",
    "02/12/2023",
    "03/12/2023",
    "04/12/2023",
    "05/12/2023",
]

ListCourse = [
    "Python",
    "Java",
    "C#",
    "PHP",
    "C++",
]

right_frame = Frame(
    ws, bd=2, relief=SOLID, padx=10, pady=10
)

Label(
    right_frame,
    text="Course Registration Form",
    font=('Times', 20),
    fg="#FFF",
    bg="#0000FF"
).grid(row=0, column=0, columnspan=2, pady=10)


Label(
    right_frame,
    text="Full Name",
    font=f,
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Email",
    font=f,
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="DOB",
    font=f,
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Gender",
    font=f,
).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Contact No.",
    font=f,
).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Select Course",
    font=f,
).grid(row=6, column=0, sticky=W, pady=10)

txt_full_name = Entry(right_frame, font=f)
txt_email = Entry(right_frame, font=f)

dob_field = OptionMenu(
    right_frame,
    dob_var,
    *ListDate
)

dob_var.set(ListDate[0])

gender_frame = LabelFrame(right_frame, padx=10, pady=10)
male_rb = Radiobutton(
    gender_frame,
    text='Male',
    variable=gender_var,
    value='male',
    font=f
)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    variable=gender_var,
    value='female',
    font=f
)

contact_field = Entry(right_frame, font=f)

select_course = OptionMenu(
    right_frame,
    sc_var,
    *ListCourse
)

def Validate_Form():
    error = "Error!"
    if txt_full_name.get() == "":
        messagebox.showerror(error, "Fullname doesn't empty")
        txt_full_name.focus_set()
        return
    
    if txt_email.get() == "":
        messagebox.showerror(error, "Email doesn't empty")
        txt_email.focus_set()
        return
    
    if dob_var.get() == "":
        messagebox.showerror(error, "DOB doesn't empty")
        return
    
    if gender_var.get() == "":
        messagebox.showerror(error, "Gender doesn't empty")
        return
    
    if contact_field.get() == "":
        messagebox.showerror(error, "Contact doesn't empty")
        contact_field.focus_set()
        return
    
    if sc_var.get() == "":
        messagebox.showerror(error, "Course doesn't empty")
        return
    
    messagebox.showinfo("Information", "Register Success")
    ws.destroy()

def Cancel_Form():
    ws.destroy()

submit_btn = Button(
    right_frame,
    text="Submit",
    bg="#00FF00",
    fg="#FFF",
    font=f,
    command=Validate_Form
)

cancel_btn = Button(
    right_frame,
    text="Cancel",
    bg="#FF0000",
    fg="#FFF",
    font=f,
    command=Cancel_Form
)

txt_full_name.grid(row=1, column=1, pady=10,padx=10)
txt_email.grid(row=2, column=1, pady=10, padx=10)
dob_field.grid(row=3, column=1, pady=10, padx=10)
select_course.grid(row=6, column=1, pady=10)
contact_field.grid(row=5, column=1, pady=10)

submit_btn.grid(row=7, column=0, pady=10,padx=10)
cancel_btn.grid(row=7, column=1, pady=10,padx=10)

right_frame.pack()
gender_frame.grid(row=4, column=1, pady=10, padx=10)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
# hello


ws.mainloop()