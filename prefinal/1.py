n = int(input())
def change(n):
    a = []
    for i in range(n):
        c = int(input())
        a.append(c)
    print(" ".join(map(str,a)))
    print("{:.2f}".format(sum(a)/len(a)))

(change(n))   