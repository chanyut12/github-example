n = int(input())
temp = float(input())
def conv_temp(n,temp):
    if n==1:
        temp = (temp*(9/5)) + 32
        return f"{temp:.2f}"
    elif n==2:
        temp  = (temp - 32) *(5/9)
        return f"{temp:.2f}" 

print(conv_temp(n ,temp))   