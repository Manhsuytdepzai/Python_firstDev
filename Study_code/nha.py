import math

def nhap():
    a = int(input("nhap a : "))
    b = int(input("nhap b : "))
    c = int(input("nhap c : "))
    return a,b,c
def giaipt(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return 'Phương trình vô số nghiệm!'
            else:
                return 'Phương trình vô nghiệm!'
        else:
            if c == 0:
                return 'Phương trình có 1 nghiệm x = 0'
            else:
                x1 = -c / b
                return 'Phương trình có 1 nghiệm x = ' ,x1
    else:
        delta = (b * b) - (4 * a * c)
    if delta < 0:
        return 'Phương trình vô nghiệm!'
    elif delta == 0:
        x1 = -b / (2 * a)
        return 'Phương trình có 1 nghiệm x = ', x1
    else:
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        return 'Phương trình có 2 nghiệm là: x1 = ', x1, 'và x2 = ', x2
def inkq(x1,x2):
        print("nghiem cua phuong trinh la x1 : ",x1, sep="")
        print("nghiem cua phuong trinh la x2 : ",x2, sep="")

a=nhap()
b=nhap()
c=nhap()
x1=giaipt(a,b,c)
x2=giaipt(a,b,c)
inkq(x1,x2)