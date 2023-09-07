n = int(input())
b = []
s = 0

for i in range(n):
    a = int(input())
    b.append(a) 

for j in b:
    s+=j

print(s - min(b))
