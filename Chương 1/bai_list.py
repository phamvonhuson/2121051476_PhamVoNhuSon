s1 = input("Nhập vào một chuỗi số cách nhau bởi khoảng trắng: ")

danh_sach_tam = s1.split()

lst = []
for x in danh_sach_tam:
    lst.append(int(x))

tong = sum(lst)

print("Ma trận 1 chiều của dãy số là:", lst)
print("Tổng của các số trong dãy là:", tong)