'''
n = int(input())
b=[]
for i in range(n):
    a = int(input())
    b.append(a)

c = int(input())

for j in b:
    if c==j:
        print(b.index(j))
        break
'''

def main():
        N = int(input())
        
        # Initialize an empty list to store N integers
        num_list = []

        # Receive N integers and store them in the list
        for i in range(N):
            num = int(input())
            num_list.append(num)

        # Receive the integer to search for
        search_value = int(input())

        # Search for the value in the list
        index = find_index(num_list, search_value)

        # Display the result
        if index != -1:
            print(find_index(num_list, search_value))
        else:
            print(-1)

def find_index(num_list, search_value):
    """
    Function to find the index of the search_value in the list.
    Returns -1 if the value is not found.
    """
    for i, num in enumerate(num_list):
        if num == search_value:
            return i
    return -1

if __name__ == "__main__":
    main()

        

