fo = open ("test.txt", "w")
fo.write("toi dang test code.")
fo.close()
# Các thuộc tính của file:
#1 kiểm tra xem file đã đóng chưa
print(fo.closed)
#2 chế độ truy cập
print(fo.mode)
#3 tên file
print(fo.name)
