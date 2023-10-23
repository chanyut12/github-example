a = int(input())
b=1
c=a-1
d=1
e=a-1
for i in range(a):
  for j in range(c):
    print("", end=" ")
  for k in range(b):
    print("", end="*")
  print()  
  b+=1
  c-=1
for i in range(a-1):
  for j in range(d):
    print("",end=" ")
  for k in range(e):
    print("",end="*")    
  print()
  d+=1
  e-=1  