import math
a=int(input())
b=int(input())
c=abs(a-b)
if a>b:
    print("A is larger than B by {}".format(c))
if b>a:
    print("A is smaller than B by {}".format(c))   
if a == b:
    print("A is equal to B")
