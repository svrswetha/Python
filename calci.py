"""Calculator"""

""" Perform basic calculations with 2 numbers"""

"""Addition"""
def add(number1, number2):
  return number1 + number2

"""Subtraction"""
def sub(number1, number2):
  return number1 - number2

"""Multiplication"""
def mul(number1, number2):
  return number1 * number2

"""Division"""
def div(number1, number2):
  try:
    return number1 / number2
  except ZeroDivisionError:
    print("Error Resolved by Zero Checking.. ")
    return 0



def RunOperations(operation, num1,num2):
  if (operation == 1):
    print("Adding....")
    print(add(num1, num2))
  elif (operation == 2):
    print("Subtracting....")
    print(sub(num1, num2))
  elif (operation == 3):
    print("Multiplying....")
    print(mul(num1, num2))
  elif (operation == 4):
    print("Division....")
    print(div(num1, num2))
  else:
    print("Idontknow")

def main():

    validInput = False
    while not validInput:
      # Get User Input
      try:
        num1 = int(input("What is number 1\n"))
        num2 = int(input("What is number 2\n"))
        operation = int(input("what do you want to do? 1)Add 2)Subtract 3)Multiply 4)Division "))
        validInput = True
      except ValueError:
        print("Invalid Input.. Try Again")
      except:
        print("unknown error")
    RunOperations(operation,num1,num2)

if __name__ == "__main__":
  main()
