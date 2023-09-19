def A():
    s = "son of A"
    print("This is A")
    print("Trying to invoke B")
    return B(s)
def B(m):
    print("Hey! this is B")
    print("I received something...")
    print("Here : ", m)
print('-----try calling A------')
A()
print('-----try calling B------')
B(__name__)