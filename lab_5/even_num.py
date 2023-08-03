def find_numbers():
    numbers = []  
    while True:
            num = int(input())
            if num == -1:
                break
            elif num%2==0: 
                numbers.append(num)

    for element in numbers:
         print(element)     

find_numbers()
