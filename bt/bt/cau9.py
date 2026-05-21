def cau_9(a, b, c):
    tong = a + b + c
    print("Tổng của ba số là:", tong)
    
    chuoi_tong = str(tong)
    dem_chan = 0
    for ky_tu in chuoi_tong:
        so = int(ky_tu)
        if so % 2 == 0:
            dem_chan = dem_chan + 1
            
    print("Trong tổng", tong, "có", dem_chan, "chữ số chẵn.")