from faker import Faker
import csv

fake = Faker()

# Tạo file CSV với 1 triệu dòng dữ liệu giả lập
filename = 'big_data.csv'
num_records = 1000000  # Số lượng bản ghi

# Mở file CSV và viết dữ liệu vào
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'address', 'email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Viết header của file CSV
    writer.writeheader()
    
    # Tạo dữ liệu giả lập và viết vào file CSV
    for i in range(num_records):
        writer.writerow({
            'id': i + 1,
            'name': fake.name(),
            'address': fake.address(),
            'email': fake.email()
        })

print(f"File {filename} đã được tạo với {num_records} bản ghi.")
