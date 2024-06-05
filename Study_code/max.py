import math
from re import X

def lasonguyento(x):
    if (x<2):
        return False
    for  i in range(2,math.sqrt(x)):
        if x % i == 0:
            return False
    return True

def sohople(x):
    if x <= 1:
        return True
    else:
        return False
def nhapvadem():
    kq=0
    print("Nhap day so:")
    while (sohople(x) is True):
        x=int(input(""))
    if(lasonguyento(x) is True):
        kq=kq+1
    return x,kq

def InKQ(kq):
    print("Co",kq,'so nguyen to')

x,kq=nhapvadem()
lasonguyento(x)
InKQ(kq)