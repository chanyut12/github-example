#input m & n
m = int(input()) #row
n = int(input()) #column

#create sum matrix [[0,0],[0,0]]
s = [[0 for j in range(n)] for i in range(m)]
matrix = []

#create function for matrix A & B
def create(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            value = int(input())
            row.append(value)
        matrix.append(row)
    return matrix

#call function
matrix_A = create(m,n)
matrix_B = create(m,n)

#output
print("Matrix A")
for i in range(m):
    for j in range(n):
        print(matrix_A[i][j], end=' ')
    print()    


print("Matrix B")
for i in range(m):
    for j in range(n):
        print(matrix_B[i][j] , end=' ')
    print()    

print("Matrix A+B")

#sum
for i in range(m):
    for j in range(n):
        s[i][j] += matrix_A[i][j] + matrix_B[i][j]

for i in range(m):
    for j in range(n):
        print(s[i][j] , end=' ')
    print()    


