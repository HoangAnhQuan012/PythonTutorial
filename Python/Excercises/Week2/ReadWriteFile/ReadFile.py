# Tạo một chương trình Python cho phép thực hiện những công việc sau:
# - Tạo ra một file text có tên là data.txt.
# - Sau đó sử dụng một vòng lặp, nhập 5 dòng văn bản vào file.
# - Đọc ra nội dung của file vừa được ghi


with open("./Excercises/Week2//ReadWriteFile/data.txt", "w") as f:
    for i in range(5):
        f.write(input("Enter a line: ") + "\n")

with open("./Excercises/Week2//ReadWriteFile/data.txt", "r") as f:
    print(f.read())


# Tạo một chương trình Python cho phép thực hiện những công việc sau:
# - Tạo ra một file text với tên được nhập vào từ bàn phím.
# - Sau đó sử dụng một vòng lặp, nhập 10 dòng văn bản vào file.
# - Đọc ra nội dung của file vừa được ghi.
# - Đếm xem trong file có bao nhiêu dòng có nội dung bắt đầu bằng chuỗi “Tony”
# - Đếm xem trong file có bao nhiêu dòng có nội dung kết thúc bằng chuỗi “Hải"
# - Có thể nhập unicode từ bàn phím

file = open('./Excercises/Week2//ReadWriteFile/text.txt', 'w', encoding='utf-8')
for i in range(10):
    file.write(input("Enter a line: ") + "\n")
file.close()

file = open('./Excercises/Week2//ReadWriteFile/text.txt', 'r', encoding='utf-8')
print(file.read())
file.close()

file = open('./Excercises/Week2//ReadWriteFile/text.txt', 'r', encoding='utf-8')
count = 0
for line in file:
    if line.startswith('Tony'):
        count += 1
print(count)
file.close()

file = open('./Excercises/Week2//ReadWriteFile/text.txt', 'r', encoding='utf-8')
count = 0
for line in file:
    if line.endswith('Hải\n'):
        count += 1
print(count)
file.close()