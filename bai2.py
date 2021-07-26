#IN dãy fibonacci


while True:
    def fibonacci():
        n= int(input("xin moi nhap vao so luong:"))
        i=1
        if n ==0:
            fbnc = []
        elif n == 1:
            fbnc = [1]
        elif n== 2:
            fbnc=[1,1]
        else:
            fbnc =[1,1]
            while  i < (n-1):

                fbnc.append(fbnc[i] + fbnc[i-1])
                i+=1
        return fbnc
    print(fibonacci())
    hoi = input("muon tiep hay khong:")
    if hoi == "k":
        break
print("BYE")



