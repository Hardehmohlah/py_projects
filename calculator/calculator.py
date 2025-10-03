def get_input():
    print("What arithmetic operation do you want to perform?(addition, subtraction, multiplication, division): ")
    to_do = input("type (q) to quit: ")
    to_do = to_do.strip().lower()
    
    return to_do

def operations(to_do):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if to_do == "addition":
        result = "The result is " + str(num1 + num2)
        print(result)
        
    elif to_do == "subtraction":
        result = "The result is " + str(num1 - num2)
        print(result)
        
    elif to_do == "multiplication":
        result = "The result is " + str(num1 * num2)
        print(result)
        
    elif to_do == "division":
        result = "The result is " + str(num1 / num2)
        print(result)
        
        

def main():
    to_do = get_input()
    
    arithmetics = ["addition", "subtraction", "multiplication", "division"]
    
    check = True
    while check:
        if to_do in arithmetics:
            check = False
        elif to_do == "q":
            check = False    
        else:
            print("nah")
            to_do = get_input()
        
    
    for arithmetic in arithmetics:
        while to_do == arithmetic:
            operations(to_do)
            
            to_do = False
    

main()