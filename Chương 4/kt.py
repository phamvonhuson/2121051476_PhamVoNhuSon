#cho file input.txt gồm các kiểu dữ liệu chữ và số. Lập trình output.txt gồm outso.txt và outchu.txt
# f = open("input.txt", "r")
# f1 = open("outso.txt", "w")
# f2 = open("outchu.txt", "w")
# s = f.readlines()
# for i in s:
#     i = i.strip().split()
#     for j in i:
#         if j.isdigit():
#             print(j, file = f1, end = " ")
#         else:
#             print(j, file = f2, end = " ")
# f.close()
# f1.close()
# f2.close()
f = open("input.txt", "r")
f1 = open("outso.txt", "w")
f2 = open("outchu.txt", "w")

cac_dong = f.readlines()

for dong in cac_dong:
    danh_sach_phan_tu = dong.strip().split()
    
    for phan_tu in danh_sach_phan_tu:
        if phan_tu.isdigit():
            print(phan_tu, file=f1, end=" ")
        else:
            print(phan_tu, file=f2, end=" ")

f.close()
f1.close()
f2.close()
