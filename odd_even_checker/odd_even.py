def main():
    value = int(input("Enter the number you want to check: "))
    test = value % 2
    
    if test == 0:
        print("Your value is even")
    else:
        print("your value is odd")
    
    
main()