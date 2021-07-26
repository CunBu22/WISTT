# chuyen doi so nguyen sang he khac

while True:
    def chuyendoi(n, B):
        if(n<0 or B<2 or B>32):
            return ""
        m = 0
        b=""
        a= n
        while a>0:
            if(B >10):
                m = a % B
                if m >= 10:
                    b = b + str(chr(50+m))
                else:
                    b = b + str(m)
            else:
                b = b + str( a % B)
            a = int(a/B)
        return "".join(reversed(b))


    n = int(input("nhap vao n:"))
    B = int(input("he so b muon chuyen"))
    print(" he so sau khi chuyen la ", n,":", chuyendoi(n,B))

    hoi = input("ban muon chuyen tiep khong:")
    if hoi == "k":
        break
print("BYE")