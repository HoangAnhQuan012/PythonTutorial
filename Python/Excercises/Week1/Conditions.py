# Viết một chương trình Python cho phép nhập vào lương, tạm ứng, phụ cấp, bảo hiểm của 
# một nhân viên sau đó tinh và in ra mức lương của người đó (lương = lương + phụ cấp –
# tạm ứng – bảo hiểm). Bảo hiểm = 5% của lương. Sau đó sẽ kiểm tra mức lương để tính 
# thuế của người đó, thuế sẽ bằng 10% của số lương phải đóng thuế (VD: Lương người đó 
# là 7000 thì người đó sẽ được miễn thuế là 5000, còn 2000 còn lại sẽ phải chịu thuế 10% 
# => Lương thực lĩnh là: 6800). Tính và in ra mức lương thực lĩnh
#

def salary_1():
    salary = int(input("Nhập lương: "))
    allowance = int(input("Nhập phụ cấp: "))
    advance = int(input("Nhập tạm ứng: "))
    insurance = salary * 0.05
    salary = salary + allowance - advance - insurance
    if salary < 5000:
        print("Lương thực lĩnh là: ", salary)
    if salary > 5000:
        tax = (salary - 5000) * 0.1
        salary = salary - tax
        print("Lương thực lĩnh là: ", salary)

salary_1()


# Viết một Chương trình Python cho phép nhập vào lương của một nhân viên (là số 
# nguyên), sau đó chương trình sẽ kiểm tra lương của người đó để tính thuế, nếu người đó 
# có lương >= 500 thì sẽ tính và in ra số tiền thuế mà nhân viên phải nộp (là 20), còn nếu 
# mức lương < 500 thì sẽ không phải nộp thuế, và sẽ in ra: “Ban khong phai nop thue”.

def tax():
    salary = int(input("Nhập lương: "))
    if salary >= 500:
        tax = 20
        print("Số tiền thuế mà nhân viên phải nộp là: ", tax)
    else:
        print("Bạn không phải nộp thuế")

tax()


# Viết chương trình nhập số giờ làm việc và lương giờ rồi tính tiền lương tổng cộng. 
# Nếu số giờ làm lớn hơn 40 thì những giờ làm dôi ra được tính 1.5 lần.
# Mở rộng
# Người lao động phải khấu trừ lại 10% thuế thu nhập cá nhân. Hãy tính ra in ra mức 
# lương trước và sau thuế của người lao động

def salary_2():
    hours = int(input("Nhập số giờ làm việc: "))
    pay = int(input("Nhập lương giờ: "))
    if hours > 40:
        salary = 40 * pay + (hours - 40) * pay * 1.5
    else:
        salary = hours * pay
    print("Mức lương trước thuế là: ", salary)
    tax = salary * 0.1
    salary = salary - tax
    print("Mức lương sau thuế là: ", salary)

salary_2()


# Viết một Chương trình cho phép tính tiền điện. Mỗi hộ gia đình sẽ được sử dụng 100 số 
# điện đầu tiên (Giá rẻ ) với giá 450D/1KW. Công thức tính tiền điện cụ thể như sau:
# Từ số 101 – 200: Giá tiền sẽ là 600/KW
# Từ số 201 – 300: Giá tiền sẽ là 750/KW
# Từ số 301 – 500: Giá tiền sẽ là 900/KW
# Từ số 501 – 1000: Giá tiền sẽ là 1000/KW
# Từ số 1000 trở lên: Giá tiền sẽ là 1200/KW
# Yêu cầu: Nhập vào số KW tiêu thụ điện. Chương trình sẽ tính và in ra tổng số tiền mà ta 
# phải nộp trước và sau khi tính thuế VAT (Thuế suất VAT = 10% tiền điện)

def electricity():
    kw = int(input("Nhập số KW tiêu thụ điện: "))
    if kw <= 100:
        price = 450
    elif kw <= 200:
        price = 600
    elif kw <= 300:
        price = 750
    elif kw <= 500:
        price = 900
    elif kw <= 1000:
        price = 1000
    else:
        price = 1200
    total = kw * price
    print("Tổng số tiền phải nộp là: ", total)
    tax = total * 0.1
    total = total + tax
    print("Tổng số tiền phải nộp sau thuế là: ", total)

electricity()

