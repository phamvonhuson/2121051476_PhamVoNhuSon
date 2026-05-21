#Viết chương trình nhập vào 2 số nguyên dương a và b, sau đó kiểm tra xem a có chia hết cho chữ số nhỏ nhất của b hay không.
#Ví dụ: a = 24, b = 582, chữ số nhỏ nhất của b là 2, và 24 chia hết cho 2
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if a > 0 and b > 0:
    chuoi_b = str(b)
    
    min_chu_so_b = int(chuoi_b[0])
    
    for ky_tu in chuoi_b:
        so = int(ky_tu)
        if so < min_chu_so_b:
            min_chu_so_b = so
            
    print("Chữ số nhỏ nhất của b là:", min_chu_so_b)

    if min_chu_so_b == 0:
        print("Không thể chia hết ")
    elif a % min_chu_so_b == 0:
        print(a, "chia hết cho", min_chu_so_b)
    else:
        print(a, "không chia hết cho", min_chu_so_b)
else:
    print("Vui lòng nguyên dương!")