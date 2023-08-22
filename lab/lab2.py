a = int(input())
b = int(input())

c = a*280
if a<4:
    c = c-100
    if b>90:
        c = c + ((b-90)*(5*a))
if a>=4:
    c = c-250
    if b>90:
        c = c + ((b-90)*(5*a))

print(c)              
