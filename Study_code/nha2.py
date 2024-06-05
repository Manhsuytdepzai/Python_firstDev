"""import math

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

x = []
def nhapvadem():
    for i in range(100):
        x =  x+ [int(input("nhap : "))]
        if(sohople(x[i])):
            break
    for i in range(x):
        if lasonguyento(x[i]):
            return x[i]
def inkq(kq):
    for i in range(x):
        print(x[i])
 

x = nhapvadem()
inkq(x)"""
import array as x
d = 0
def LaSoNguyenTo(x):
    for i in range(1,x):
        if x%i==0:
            return False
    return True
def SoHopLe(x):
    if x<=1:
        return True
    return False
def NhapVaDem():
    x = [100]
    global d
    print('Nhap day so:')
    while True:
        for i in range(100):
            x =  x+ [int(input("nhap : "))]
            if SoHopLe(x[i])==True:
                break 
            for i in range(100):        
                if LaSoNguyenTo(i):
                    d=d+1
                    return d
                
def Inkq(d):
    print('Co ',d,' so nguyen to')
NhapVaDem()
Inkq(d)
    
