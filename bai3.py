#Kiểm tra số nguyên tố
while True:
    n = int(input("nhap vao so nguyen duong n:"))
    dem =0
    for i in range(1, n+1):
        if (n % i ==0):
            dem += 1
    if dem ==2:
        print("n la so nguyen to :")
    else:
        print("n khong la so nguyen to:")
    tiep=input("ban co muon nhap tiep khong?")
    if tiep == "khong":
        break
print("GOODBYE")

