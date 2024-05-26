x = int(input("number: "))
def print_sequence(x):
    for i in range(1, x+1):
        if i%2==0 and i%3==0:
            print("TwoThree")
        elif i%2==0:
            print("Two")
        elif i%3==0:
            print("Three")
        elif i%2!=0 and i%2!=0:
            print(i)
            
print_sequence(x)