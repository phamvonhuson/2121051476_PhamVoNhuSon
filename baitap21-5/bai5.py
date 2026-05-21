#viết chg trình nhập 2 số nguyên dương m,n kiểm tra xem m có chia hết tổng chữ số của n không?
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))

if m > 0 and n > 0:
    n_chuoi = str(n)
    tong_chu_so_n = 0
    
    for ky_tu in n_chuoi:
        tong_chu_so_n = tong_chu_so_n + int(ky_tu)
    
    print("Tổng các chữ số của n là:", tong_chu_so_n)

    if m % tong_chu_so_n == 0:
        print(m, "có chia hết cho", tong_chu_so_n)
    else:
        print(m, "không chia hết cho", tong_chu_so_n)

else:
    print("không thỏa mãn m và n là số nguyên dương!")