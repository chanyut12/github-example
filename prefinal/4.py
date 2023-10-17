ins = str(input()).split()
n = int(ins[0])
m = int(ins[1])
# n, m= [int(x) for x in input().split()]
# print(n,m)
a = [[0 for x in range(n)] for y in range(m)] 
b = [[0 for x in range(n)] for y in range(m)] 
for i in range(n):
    k = input().split( )
    for j in range(m):
        b[i][j]=k[j]
        a[i][j]=k[j]

for i in range(n):
    for j in range(m):
        if a[i][j] =='*':
            b[i+1][j] = '*'

for i in range(n):
    for j in range(m):
        print(b[i][j] , end=' ')
    print()



    
