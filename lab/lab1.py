a = float(input())
b = float(input())
c = a + a*0.07
if b>=c:
    print("{:.2f}".format(a))
    print("{:.2f}".format(c))
    print("{:.2f}".format(b))
    print("{:.2f}".format(b-c))
else:
    print("The money checking again")

