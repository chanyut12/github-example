n = int(input())
b = []
c = 0
for i in range(n):
    a = int(input())
    b.append(a)

for j in b:
    if j>50:
        c+=1

print(c)

