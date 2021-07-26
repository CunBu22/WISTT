#Kiem tra doi xung


def Kiemtra(s):
    flag= True
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            flag= False
            break
    return flag
def main():
    print("nhap vao chuoi:")
    s= input()
    if(Kiemtra(s)):
        print("chuoi ban nhap doi xung:")
    else:
        print("chuoi ban nhap khong doi xung:")

while True:
    main()
    print("ban co muon nhap tiep khong?")
    s= input()
    if s=="1":
        break
print("GOODBYE")

