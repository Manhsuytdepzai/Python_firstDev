"""print("nhap ten : ")
name = input()
print("xin chao " + name)
x = int(input())
y = int(input())
print("x > y:", x > y)"""
#b2
"""a = int(input())
Total = int(input())

Total += a # Using += Operator
print("The Value of the Total after using += Operator is:", Total)
Total -= a # Using -= Operator
print("The Value of the Total after using -= Operator is:", Total)
Total *= a # Using *= Operator
print("The Value of the Total after using *= Operator is:", Total)
Total //= a # Using //= Operator
print("The Value of the Total after using //= Operator is:", Total)
Total **= a # Using **= Operator
print("The Value of the Total after using **= Operator is:", Total)
Total /= a # Using /= Operator
print("The Value of the Total after using /= Operator is:", Total)
Total %= a# Using %= Operator
print("The Value of the Total after using %= Operator is:", Total)"""
#x = input()
#print('H' in x or 'h' in x)
"""age = int(input())
print("Your cat is young") if age < 5 else print("Your cat is old")"""
a = int(input())
b = int(input())
c = int(input())
tb = (a+b+c)/3
if tb > a and tb > b:
    print("ab")
elif tb > a and tb > c:
    print("ac")
elif tb > b and tb > c: 
    print("bc")
elif tb > a:
    print("a")
elif tb > b:
    print("b")
elif tb > c:
    print("c")    
