#viết chương trình nhập vào 1 số nguyên dương n, kiểm tra xem tích các chữ số của n có phải là số chẵn và lớn hơn 20 không?

n_chuoi = input("Nhập n: ")

tich_chu_so = 1

for ky_tu in n_chuoi:
    tich_chu_so *= int(ky_tu)

print(f"Tích các chữ số của {n_chuoi} là: {tich_chu_so}")

if tich_chu_so % 2 == 0 and tich_chu_so > 20:
    print(f"Kết quả: {tich_chu_so} chia hết cho 2 và lớn hơn 20.")
else:
    print(f"Kết quả: {tich_chu_so} không thỏa mãn điều kiện.")