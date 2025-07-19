#for loop
#multiplication_table.py
# Prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))
for x in range (1, 11) :
  result = number * x
  print(f"{number}*{x} = {result}")

