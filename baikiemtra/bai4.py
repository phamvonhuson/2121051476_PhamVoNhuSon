#Viết chg trình nhập 2 số nguyên dương a ,b.Tính tổng a+b và in ra chữ số lớn nhất trong tổng đó
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a > 0 and b > 0:
    tong = a + b
print("Tổng (", a, "+", b, ") =", tong)
tong1 = str(tong)
max = int(tong1[0])

for ky_tu in tong1:
    so = int(ky_tu)
    if so > max:
        max = so

print("Chữ số lớn nhất là:", max)