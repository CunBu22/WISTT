# nhập vào chuỗi nhị phân in ra chuỗi chia het cho 5



while True:
    val = []
    item=[x for x in input("nhap vao day so: ").split(',')]

    for p in item:
        t = int(p, 2)
        if not t % 5:
            val.append(p)
    print (','.join(val))
    hoi = input("muon nhap nua khong:")
    if hoi == "khong them":
        break
print("BYE")
