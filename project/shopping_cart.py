#shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit):')
    if food.lower() =="q":
        break
    else:
        price = float(input(f"Enter the price of a {food} : $"))
        foods.append(food)
        prices.append(price)

print("___________Your cart_____________________")
print("Your order have : " ,end='')

for food in foods:
    if food == foods[-1]:
        print(f"and {food} so",end=" ")
    else:
        print(f"{food} ," ,end=" ")    

for price in prices:
    total = price + total


print(f"Your total is: ${total}")    