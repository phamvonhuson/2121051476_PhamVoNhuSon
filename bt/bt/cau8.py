# Câu 8 Viết chương trình nhập vào ba số nguyên dương x, y, z, sau đó tìm xem tích (x * y * z) có mấy chữ số và chữ số lớn nhất bằng bao nhiêu.

# File: bt.py
def cau_8(x, y, z):
    tich = x * y * z
    print("Tích của ba số là:", tich)

    chuoi_tich = str(tich)

    so_chu_so = len(chuoi_tich)
    print("Tích có tất cả", so_chu_so, "chữ số.")

    max_chu_so = int(chuoi_tich[0])
    
    for ky_tu in chuoi_tich:
        so = int(ky_tu)
        if so > max_chu_so:
            max_chu_so = so
            
    print("Chữ số lớn nhất trong tích là:", max_chu_so)
