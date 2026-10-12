def addition():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    sum=a+b
    print(sum)
    
def subtraction():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    difference =a-b
    print(difference)

def multiplication():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    product =a*b
    print(product)
    
def division():
    while True:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if b == 0:
            print("Division by zero is not possible. Enter a valid number.")
        else:
            result = a / b
            print(result)
            break
    

def percentage():
    while True:
        a = int(input("Enter the number whose percentage is required: "))
        b = int(input("Enter the number you want to keep as reference: "))

        if b == 0:
            print("Reference number cannot be zero. Enter again.")
        else:
            percentage = a / b * 100
            print(percentage, "%")
            break
def status():
    num = int(input("Enter your number: "))
    if (num==0):
        print("Entered number is zero(neither even nor odd)")
    elif(num%2==0):
        print("Entered number is even.")
    else:
        print("Entered number is odd.")

print("Welcome! Choose an option from below to start using calculator.\n")
print("1. Addition of two numbers")
print("2. Subtraction of two numbers")
print("3. Multiplication of two numbers.")
print("4. Division of two numbers.")
print("5. Check if a number is even or odd.")
print("6. Percentage of a number with respect to another number.")
print("7. Exit.")
print("\n")

while True:
    choice=int(input("Enter your choice:"))
    print(" ")
    
    match choice:
        case 1:
            print("It will sum two numbers.")
            addition()
        case 2:
            print("It will subtract two numbers.")
            subtraction()
        case 3:
            print("It will multiply two numbers.")
            multiplication()
        case 4:
            print("It will divide two numbers.")
            division()
        case 5:
            print("It will check if number is even or odd.")
            status()
        case 6:
            print("It will give percentage of one number with respect to another.")
            percentage()   
        case 7:
            print("Thank you for using calculator. We are exiting this program.")
            break
        case _:
            print("Invalid choice! Try again.")

   

    
    
