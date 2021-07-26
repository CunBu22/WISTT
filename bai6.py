# tính giai thừa khong dung for


while True:

    n = int(input("nhap vao so can tinh:"))

    def a(n):
        if n == 0:
            return 1
        else:
            return n * a(n-1)
    print(a(n))
    tiep = input("ban co muon tiep hay khong")
    if tiep == "k":
        break
print("BYE")