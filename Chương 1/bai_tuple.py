#BT: Nhập matran 4x3 dưới dạng tuple:
temp_matrix = []

print("Nhập ma trận 4x3 (mỗi hàng 3 số cách nhau bởi khoảng trắng):")

for i in range(4):
    row_input = input("Nhập hàng " + str(i + 1) + ": ")
    
    row_tuple = tuple(int(x) for x in row_input.split())
    
    temp_matrix.append(row_tuple)

matran_tuple = tuple(temp_matrix)

# In kết quả
print("Ma trận tuple vừa nhập:")
print(matran_tuple)
