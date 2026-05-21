#iết chương trình nhập vào một dãy số thực x1, x2, …, xn (0 < n < 100), sau đó tìm trung bình cộng các phần tử âm trong dãy mà giá trị nằm trong khoảng (-1000, -10)
n = int(input("Nhập số phần tử n (0 < n < 100): "))

if 0 < n < 100:
    day_so = []
    for i in range(n):
        print("Nhập x", i + 1, ":", end=" ")
        so = float(input())
        day_so.append(so)

    tong_am = 0
    dem_am = 0

    for x in day_so:
        if -1000 < x < -10:
            tong_am = tong_am + x
            dem_am = dem_am + 1

    if dem_am > 0:
        tbc = tong_am / dem_am
        print("Trung bình cộng các số âm thỏa mãn là:", tbc)
    else:
        print("Không có số âm nào nằm trong khoảng (-1000, -10).")

else:
    print("Số lượng phần tử n không hợp lệ!")