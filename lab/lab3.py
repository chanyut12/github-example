c = 0
while True:
    a = int(input())
    if a==1:
        c = c+100
    elif a==2:
        c = c+80
    elif a==3:
        c = c+50
    elif a==4:
        c = c+200
    else:
        break                
print(c)