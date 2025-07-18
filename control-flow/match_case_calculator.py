# match_case_calculator
#prompt the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#prompt for the type of operation
operation = input("Choose the operation (+, -, *, /):.")
#math case
match operation:
  case "+":
    result = num1 + num2
    print(f"The result is {result}.")
  case "-":
    result = num1 - num2
    print(f"The result is {result}.")
  case "*":
    result = num1 * num2
    print(f"The result is {result}.")
  case "/":
    if num2 != 0:
      result = num1 / num2
      print(f"The result is {result}.")
    else :
      print("Error: Division by zero is not allowed.")
  case _:
    print(f"Invalid input")
