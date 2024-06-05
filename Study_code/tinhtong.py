# Tạo hàm đệ quy tính tổng
def tinh_tong(n):
    if (n == 1):
        return 1
    return n + tinh_tong(n - 1)
 
 
# Chương trình chính
print("Hãy nhập vào số n: ")
n = int(input())
tong = tinh_tong(n)
print("Tổng là: ", tong)"""
"""def tich(n):
    if n==1:
        return 1
    return n * tich(n-1)

n = int(input("nhap n : "))
tich = tich(n)
print("tich la ")"""
def tich(n):
    if n==1:
        return 1
    return (1/n) * tich(n-1)

n = int(input("nhap n : "))
tich = tich(n)
print("tich la ",tich)