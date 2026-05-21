#viết chương trình đọc tệp input.txt gồm n dòng, mỗi dòng là 1 số tự nhiên. kết quả chương trình là output gồm n dòng lần lượt là các ước số nguyên tố khác nhau
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

f = open("input.txt", "r")
f_out = open("output.txt", "w")

cac_dong = f.readlines()

for dong in cac_dong:
    so = int(dong.strip())
    
    uoc_nt = []
    
    for i in range(2, so + 1):
        if so % i == 0 and la_so_nguyen_to(i):
            uoc_nt.append(str(i))
    
    ket_qua = " ".join(uoc_nt)
    f_out.write(ket_qua + "\n")

f.close()
f_out.close()


