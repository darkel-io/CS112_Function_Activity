def multiplication():
    if num1 == num2 != num3:
        prd = (num1 * num2) + num3
        print(f"The result is: {prd}")
    elif num2 == num3 != num1:
        prd = (num2 * num3) + num1
        print(f"The result is: {prd}")
    elif num1 == num3 != num2:
        prd = (num1 * num3) + num2
        print(f"The result is: {prd}")
    elif num1 != num2 != num3:
        add = num1 + num2 + num3
        print(f"The result is: {add}")
    elif num1 == num2 == num3:
        prd = num1 * num2 * num3
        print(f"The result is: {prd}")
    else:
        print("Invalid output.")


num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
num3 = eval(input("Enter third number: "))

multiplication()