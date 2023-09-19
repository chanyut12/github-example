base = float(input())
height_ = float(input())
def cellTriagle(base , height_):
    a = 0.5 * base * height_
    return f"{a:.2f}"

print(cellTriagle(base, height_))