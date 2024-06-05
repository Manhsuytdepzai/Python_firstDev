import math

def nhap():
    n = int(input("nhap n = "))
    return n
def inkq(n):
    while True:
        for i in range(n):
            if i%2 == 0:
                print(i)
        x = input("nhap : ") 
        if x == 'k':
            break
        else:
            return n
#
n=nhap()
inkq(n)        