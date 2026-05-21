# Viết chương trình nhập vào một dãy số thực x1, x2, …, xn (0 < n < 100), sau đó tìm trung bình cộng các phần tử dương trong dãy mà giá trị nằm trong khoảng (0, 1000)
n = int(input("Nhập số phần tử: "))

if 0 < n < 100:
    day_so = []
    for i in range(n):
        so_thuc = float(input(f"Nhập x{i+1}: "))
        day_so.append(so_thuc)

    tong = 0
    dem = 0

    for x in day_so:
        if 0 < x < 1000:
            tong += x
            dem += 1

    if dem > 0:
        tbc = tong / dem
        print(f"Trung bình cộng các số trong khoảng (0, 1000) là: {tbc}")
    else:
        print("Không có số nào trong dãy nằm trong khoảng (0, 1000).")
else:
    print("Giá trị n không hợp lệ.")