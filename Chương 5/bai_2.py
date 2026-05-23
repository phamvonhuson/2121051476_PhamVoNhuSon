#Viết chương trình nhập vào một dãy số nguyên x1, x2, …, xn (0 < n < 200), tính tổng các phần tử chẵn trong dãy, và kiểm tra xem tổng này có chia hết cho 7 và nhỏ hơn 200 hay không
n = int(input("Nhập số lượng phần tử n (0 < n < 200): "))

if 0 < n < 200:
    day_so = []
    
    for i in range(n):
        print("Nhập x", i + 1, ":", end=" ")
        so = int(input())
        day_so.append(so)

    tong_chan = 0
    for x in day_so:
        if x % 2 == 0:
            tong_chan = tong_chan + x
            
    print("Tổng các phần tử chẵn là:", tong_chan)

    if tong_chan % 7 == 0 and tong_chan < 200:
        print("Kết quả: Tổng thỏa mãn điều kiện (chia hết cho 7 và < 200)")
    else:
        print("Kết quả: Tổng không thỏa mãn đồng thời hai điều kiện")
else:
    print("Số lượng phần tử n không hợp lệ!")