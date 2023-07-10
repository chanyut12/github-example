name=input()
weight=int(input()) #kg
height=int(input()) #centimeter
#convert cm -> m
height = height/100
bmi = weight/(height**2)
print("Name={}".format(name))
print("BMI={:.2f}".format(bmi))

