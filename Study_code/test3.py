import math
def lasonguyento(x):
    if (x<2):
        return False
    for  i in range(2,math.sqrt(x)):
        if x % i == 0:
            return False
        else :   
            return True
def SoHopLe(x):
    if x <= 1:
        return True
    return False
def NhapVaDem():
    global d
    d=0
    x = []
    lenth = len(x)
    print('Nhap day so:')
    while True:
        x=int(input(""))
        if SoHopLe(x) is True:
            break
        for i in range(1, lenth):
            if lasonguyento(x[i]) is True:
                d=d+1
                return d
def Inkq(d):
    print('Co ',d,' so nguyen to')
d=NhapVaDem()
Inkq(d)