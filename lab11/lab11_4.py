from math import gcd
y = int(input())
x = int(input())
def gcd_(y,x):
    if y>x:
        return gcd(y,x)
    elif y == 0:
        return x
    return gcd_(y,x%y)

print(gcd_(y,x))