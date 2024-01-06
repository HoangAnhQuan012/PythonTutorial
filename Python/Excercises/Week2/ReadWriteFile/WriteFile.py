# Tạo một chương trình Python cho phép thực hiện những công việc đọc ghi file như sau:
# - Tạo ra một file text có tên là fruits.txt.
# - Hãy khai báo một list gồm 10 phần tử, mỗi phần tử chứa tên của một loại trái cây bằng 
# tiếng anh, sau đó ghi cả list này vào file sử dụng hàm writelines()
# - Sau đó, hãy đọc nội dung của file và hiển thị ra chương trình, sử dụng hàm readlines()
# - Hãy đếm xem có bao nhiêu dòng trong file có nội dung bắt đầu bằng chữ ‘b’ và in kết 
# quả.
# - Hãy đếm xem có bao nhiêu dòng trong file có nội dung kết thúc bằng chữ ‘a’ và in ra 
# kết quả

file = open('./Excercises/Week2//ReadWriteFile/fruits.txt', 'w')
fruits = ['banana\n', 'orange\n', 'apple\n', 'kiwi\n', 'melon\n', 'mango\n', 'pear\n', 'grape\n', 'pineapple\n', 'peach\n']
file.writelines(fruits)
file.close()

file = open('./Excercises/Week2//ReadWriteFile/fruits.txt', 'r')
print(file.readlines())
file.close()

file = open('./Excercises/Week2//ReadWriteFile/fruits.txt', 'r')
count = 0
for line in file:
    if line.startswith('b'):
        count += 1
print(count)
file.close()

file = open('./Excercises/Week2//ReadWriteFile/fruits.txt', 'r')
count = 0
for line in file:
    if line.endswith('a'):
        count += 1
print(count)