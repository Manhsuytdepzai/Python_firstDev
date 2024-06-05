def lasonguyento(x):
    if (x<2):
        return False
    for  i in range(2,math.sqrt(x)):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    if lasonguyento(n) is True:
        tong += n
    if(n==0):
        break
    tong = 0
    if lasonguyento(n) is True:
        tong += n
print("tong : ",tong)
    