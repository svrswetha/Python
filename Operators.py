

"""Addition"""

"""Addition"""
def add(number1,number2):
    return number1 + number2

"""Subtraction"""
def subtract(number1, number2):
    return number1 - number2


"""Multiplication"""
def multiply(number1, number2):
    return number1 * number2


"""Division"""
def division(number1,number2):
    return number1/number2

def main():
    num1 = int(input("Enter Number 1"))
    num2 = int(input("Enter Number 2"))

    print add(num1,num2)
    print subtract(num1,num2)
    print multiply(num1,num2)
    print division(num1,num2)

main()