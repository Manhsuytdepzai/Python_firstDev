#ong cac so tu 1,n
"""n = int(input())
s=0
for i in range(1, n+1):
    s += i
print(s) """
#in ten
"""name = input()
for i in name:
    print(i)"""
#tong cac so le tu a,b
"""a = int(input())
b = int(input())
tongle = 0
for i in range(a, b+1):
    if i%2 != 0 :
        tongle+=i
print(tongle)"""
#in tat ca cac ki tu khac 'y'
"""s = input()
for i in s:
    if i != 'y':
        print(i)"""
#so chan tu 1,20
"""for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)"""
#bang cuu chuong
"""a = int(input())
for i in range(1,11):
    print(a, " * ", i, "= ", a*i)"""
#so chan so le trong khoang a, b
"""a = int(input())
b = int(input())
sole = 0
sochan = 0
for i in range(a,b+1):
    if i%2 == 0:
        sochan += 1
    else:
        sole += 1
print("sochan : ", sochan)
print("sole : ", sole)"""
#lay sau dau phay 2 chu so
"""n = int(input())
s = 0
for i in range(1,n+1):
    s += i/(i+1)
print(round(s,2))"""
#gia tri nho nhat trong mang
"""print("nhap so phan tu mang : ",end= '')
n = int(input())
a = []
print("nhap phan tu mang : ")
for i in range(n):
    a.append(int(input()))            
min = a[0]
for i in a:
    if i < min: 
        min = i
print("so nho nhat trong mang : ", min)"""
#tong gia tri cac phan tu trong mang
"""print("nhap so phan tu mang : ",end= '')
n = int(input())
a = []
print("nhap phan tu mang : ")
for i in range(n):
    a.append(int(input()))
s = 0
for i in a:
    s += i
print("tong cac phan tu  : ", s)"""
#sap xep tang dan, giam dan
"""print("nhap so phan tu mang : ",end= '')
n = int(input())
a = []
print("nhap phan tu mang : ")
for i in range(n):
    a.append(int(input()))
a.sort()
print(a)   
a.sort(reverse=True)
print(a)"""
#in so le trong mang
"""print("nhap so phan tu mang : ",end= '')
n = int(input())
a = []
print("nhap phan tu mang : ")
for i in range(n):
    a.append(int(input()))
for i in a:
    if i%2 != 0:
        print(i,end= '')"""
#so chia het cho 5
"""print("nhap so phan tu mang : ",end= '')
n = int(input())
a = []
print("nhap phan tu mang : ")
for i in range(n):
    a.append(int(input()))
for i in a:
    if i%5 == 0:
        print(i, end= ' ')"""
#viet hoa ten
"""name = input()
print(name.upper())"""
#chuyen hoa thanh thuong
"""name = input()
print(name.lower())"""
#tach chuoi
"""chuoi = input()
print(chuoi.split(" "))"""
#in 2 ki tudau va 2 ki tu cuoi cua chuoi
"""print("nhap chuoi : ",end= '')
s = input()
if len(s)<2:
    print("chuoi rong ")
else: 
    print(s[0:2] + s[-2:])"""
#doi vi tri 2 ki tu dau r noi
"""s1 = input()
s2 = input()

tmp = s1[0:2] + s2[2:]
s1 = s2[0:2] + s1[2:]
s2 = tmp

print(s1 + " " + s2)"""
#lũy thưaf tăng dần
"""n = int(input("nhap day so : "))
d = dict()
for i in range(n):
    d[i]=i*i
print(d)"""
a=input("Nhập vào các giá trị:")
l=a.split(" ")
t=tuple(l)
print (l)
print (t)

