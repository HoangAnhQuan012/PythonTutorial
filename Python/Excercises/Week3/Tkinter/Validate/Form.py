from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title("Python Desktop App")
ws.config(bg="#0B5A81")

f = ('Times', 14)
var = StringVar()
var.set('male')

countries = []
variable = StringVar()

world = open("./Excercises/Week3//Tkinter/Validate/countries.txt", "r", encoding="utf-8")
for country in world:
    country = country.rstrip("\n")
    countries.append(country)

right_frame = Frame(
    ws, bd=2, relief=SOLID, padx=10, pady=10
)

Label(
    right_frame,
    text="Họ tên:",
    bg="#CCCCCC",
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Email:",
    bg="#CCCCCC",
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Điện thoại:",
    bg="#CCCCCC",
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Giới tính:",
    bg="#CCCCCC",
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Quốc gia:",
    bg="#CCCCCC",
    font=f
).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Password:",
    bg="#CCCCCC",
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Re-Ener Password:",
    bg="#CCCCCC",
    font=f
).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(right_frame, bg="#CCCCCC", padx=10, pady=10)

txtName = Entry(right_frame, font=f)
txtEmail = Entry(right_frame, font=f)
txtMobile = Entry(right_frame, font=f)

male_rb = Radiobutton(gender_frame, text="Nam", bg="#CCCCCC", variable=var, value='male', font=('Times', 10))
female_rb = Radiobutton(gender_frame, text="Nữ", bg="#CCCCCC", variable=var, value='female', font=('Times', 10))
others_rb = Radiobutton(gender_frame, text="Khác", bg="#CCCCCC", variable=var, value='others', font=('Times', 10))

register_country = OptionMenu(right_frame, variable, *countries)
register_country.config(width=15, font=('Times', 12))

txtPassword = Entry(right_frame, font=f, show="*")
txtConfirmPassword = Entry(right_frame, font=f, show="*")

def Validate_Form():
    error = "Error!"
    if txtName.get() == "":
        messagebox.showerror(error, "Họ tên không được để trống")
        txtName.focus_set()
        return
    
    if txtEmail.get() == "":
        messagebox.showerror(error, "Email không được để trống")
        txtEmail.focus_set()
        return
    
    if txtEmail.get().find("@") == -1 or txtEmail.get().find(".") == -1:
        messagebox.showerror(error, "Email không hợp lệ")
        txtEmail.focus_set()
        return
    
    if txtMobile.get() == "":
        messagebox.showerror(error, "Điện thoại không được để trống")
        txtMobile.focus_set()
        return
    
    if txtMobile.get().isnumeric() == False:
        messagebox.showerror(error, "Điện thoại phải là ký tự số")
        txtMobile.focus_set()
        return
    
    if var.get() == "":
        messagebox.showerror(error, "Giới tính không được để trống")
        return
    
    if variable.get() == "":
        messagebox.showerror(error, "Quốc gia không được để trống")
        return
    
    if txtPassword.get() == "":
        messagebox.showerror(error, "Password không được để trống")
        txtPassword.focus_set()
        return
    
    if txtConfirmPassword.get() == "":
        messagebox.showerror(error, "Re-Enter Password không được để trống")
        txtConfirmPassword.focus_set()
        return
    
    if txtPassword.get() != txtConfirmPassword.get():
        messagebox.showerror(error, "Password và Re-Enter Password không giống nhau")
        txtPassword.focus_set()
        return
    messagebox.showinfo("Success!", "Đăng ký thành công")
    
register_btn = Button(right_frame, text="Register", font=f, relief=SOLID, cursor='hand2', command=Validate_Form)

txtName.grid(
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

txtMobile.grid(
    row=2,
    column=1,
    pady=10,
    padx=20
)

register_country.grid(
    row=4,
    column=1,
    pady=10,
    padx=20
)

txtPassword.grid(
    row=5,
    column=1,
    pady=10,
    padx=20
)

txtConfirmPassword.grid(
    row=6,
    column=1,
    pady=10,
    padx=20
)

register_btn.grid(
    row=7,
    column=1,
    pady=10,
    padx=20
)

right_frame.pack()

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)

ws.mainloop()