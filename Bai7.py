# tro choi doan so


import random
import numpy as np


def nul(nun, u):
    dola = 0
    trai_ot = 0
    for i in range(len(nun)):
        if u[i]== nun[i]:
            dola +=1
        else:
            if u[i] in nun:
                trai_ot +=1
    return dola, trai_ot
if __name__ == '__main__':
    playing = True
    nun= str(random.randint(0000, 9999))
    b =0
    print("Chào mừng đến với trò chơi đoán vui có thưởng  :")
    print("Khi đoán đúng một chữ số đúng vị trí bạn sẽ có một 1 đô la và đoán sai bạn sẽ được một trái ớt :")
    print(" Bat dau nao!!!!!!!")
    while playing:
        u = input("Xin mời chọn số: ")
        if u == " không chơi":
            break
        if len(u)!=4:
            print("Bạn đoán chưa đúng, chúc may mắn lần sau:")
            continue
        dola, trai_ot = nul(nun, u)
        b+=1

        print(f"ban co {str(dola)}  cow, va {str(trai_ot)} bull")
        if u == nun:
            playing=False