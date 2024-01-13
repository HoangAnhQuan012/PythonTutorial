from faker import Faker
from pyspark.sql import SparkSession

# Khởi tạo SparkSession
spark = SparkSession.builder.appName('example').getOrCreate()

# Tạo một số lượng lớn dữ liệu giả lập
fake = Faker()
num_records = 1000000  # Số lượng bản ghi

# Tạo DataFrame với dữ liệu giả lập
data = []
for _ in range(num_records):
    data.append({
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'phone_number': fake.phone_number(),
        # Thêm các trường dữ liệu khác tùy ý
    })

df = spark.createDataFrame(data)

# Hiển thị dữ liệu
# df.show()
print(f"Tổng số bản ghi: {df.count()}")
