#viết chương trình nhập vào 1 số nguyên dương n, kiểm tra xem tổng các chữ số của n có phải là số chia hết cho 3 không?

n_chuoi = input("Nhập n: ")

tong_chu_so = 0

for ky_tu in n_chuoi:
    tong_chu_so += int(ky_tu)

print(f"Tổng các chữ số của {n_chuoi} là: {tong_chu_so}")

if tong_chu_so % 3 == 0:
    print(f"Kết quả: {tong_chu_so} chia hết cho 3.")
else:
    print(f"Kết quả: {tong_chu_so} không chia hết cho 3.")