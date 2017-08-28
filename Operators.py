"""Calculator"""

"""Addition"""

def add(number1,number2):
    return number1 + number2

"""Subtraction"""
def sub(number1, number2):
    return number1 - number2


"""Multiplication"""
def mul(number1, number2):
    return number1 * number2


"""Division"""
def div(number1,number2):
    return number1/number2

def main():
    num1 = int(input("Enter Number 1\n"))
    num2 = int(input("Enter Number 2\n"))
    operation =raw_input("what do you want to do? 1)Add 2)Subtract 3)Multiply 4)Division")

    if(operation ==  '1'):
        print(add(num1,num2))
    elif(operation == '2'):
        print(sub(num1,num2))
    elif(operation == '3'):
        print(mul(num1,num2))
    elif(operation == '4'):
        print(div(num1,num2))
    else:
        print("Idontknow")

main()