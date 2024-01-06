from tkinter import *

root = Tk()
root.title('Form đăng ký')
root.geometry('400x300')

var1 = StringVar()
var2 = StringVar()
varResult = StringVar()

def clearform():
    var1.set('')
    var2.set('')
    varResult.set('')

def tinhtong():
    so1 = int(var1.get())
    so2 = int(var2.get())
    ketqua = so1 + so2
    varResult.set(str(ketqua))

lblNum1 = Label(root, text='Số thứ nhất:').place(x = 20, y = 40)
txtNum1 = Entry(root, textvariable=var1, width=30).place(x = 100, y = 40)

lblNum2 = Label(root, text='Số thứ hai:').place(x = 20, y = 80)
txtNum2 = Entry(root, textvariable=var2, width=30).place(x = 100, y = 80)

lblResult = Label(root, text='Kết quả:').place(x = 20, y = 120)
txtResult = Entry(root, textvariable=varResult, width=30).place(x = 100, y = 120)

btnSave = Button(root, bg = 'white', fg = 'green', text='Tính toán', command=tinhtong).place(x = 50, y = 160)
btnClear = Button(root, text='Nhập lại', command=clearform).place(x = 120, y = 160)


root.mainloop()