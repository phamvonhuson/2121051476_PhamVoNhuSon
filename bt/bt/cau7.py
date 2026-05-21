# Câu 7 Viết chương trình nhập vào một dãy số nguyên x1, x2, ..., xn (0 < n < 100), tính tổng các phần tử là số nguyên tố trong dãy, và kiểm tra xem tổng này có phải là số lẻ và lớn hơn 50 hay không.
# Hàm kiểm tra một số có phải số nguyên tố hay không

def la_so_nguyen_to(k):
    """Hàm kiểm tra một số có phải số nguyên tố hay không"""
    if k < 2:
        return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True

def cau_7(n):
    """Hàm nhập dãy số và xử lý theo yêu cầu câu 7"""
    day_so = []
    for i in range(n):
        print("Nhập x", i + 1, ":", end=" ")
        so = int(input())
        day_so.append(so)

    tong_nt = 0
    for x in day_so:
        if la_so_nguyen_to(x):
            tong_nt = tong_nt + x
            
    print("Tổng các số nguyên tố trong dãy là:", tong_nt)

    if tong_nt % 2 != 0 and tong_nt > 50:
        print("Kết quả: Tổng thỏa mãn (là số lẻ và > 50)")
    else:
        print("Kết quả: Tổng không thỏa mãn đồng thời hai điều kiện")