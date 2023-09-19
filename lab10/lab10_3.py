w = int(input())
h = int(input())
def isEqual(w,h):
    if w==h:
        print("YES")
        print("Area is",calArea(w,h))
    else:
        print("NO")

def calArea(w,h):
    return w*h
    
    
isEqual(w,h) 