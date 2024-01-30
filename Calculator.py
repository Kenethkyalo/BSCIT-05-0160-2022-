Num1 = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
Num2 = int(input("Enter the second number: "))
result = 0
if operator == '+':
 result = Num1 + Num2
 print('Result: ', result)
elif operator == '-':
  result = Num1 - Num2
  print('Result: ', result)
elif operator == '*':
  result = Num1 * Num2
  print('Result: ', result)
elif operator == '/':
  result = Num1 / Num2
  print('Result: ', result)
else:
  print("Invalid operator")