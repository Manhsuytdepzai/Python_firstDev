#tính giai thừa 1 số
"""n = int(input("nhap 1 so : "))
giaithua = 1
for i in range(1,n+1):
    giaithua *= i

print(n,"! = ",giaithua)"""
#chia het cho bay nhung k phai boi cua 5
"""for i in range(10,201):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=',')"""
#dictionary
"""n = int(input("nhap 1 so : "))
d = dict()
for i in range(n+1):
    d[i]=i*i
print(d)"""
#ktra so nguyen to
"""n = int(input("nhap 1 so : "))
dem = 0
if n<2:
    print(n,"khong la so nguyen to")
else:
    for i in range(1, n+1):
        if n%i == 0:
            dem+=1
if dem==2:
    print(n,"la so nguyen to")
else:
    print(n,"khong la so nguyen to")"""
#in so nguyen to trong khoang n
"""n = int(input("nhap 1 so : "))
dem = 0
if n<2:
    print(n,"khong co so nguyen to")
else:
    for i in range(1, n+1):
       [
            for j in range(1,i+1):
            if i%j == 0:
                dem += 1
        if dem==2:
            print(i)
sss
       ]"""
import math

def nhap():
    n = int(input("nhap n = "))
    return n
def inkq(n):
    while True:
        for i in range(1,n+1):
            if i%2 == 0:
                print(i)
        x = input("nhap : ") 
        if x == 'k':
            print("ket thuc")
            break
        else:
            return n
n=nhap()
inkq(n)  