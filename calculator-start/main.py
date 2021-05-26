from art import logo

def switcher(first,operation,second):
  switch = {
    operation == '+':first + second,
    operation == '-':first -second,
    operation == '*':first * second,
    operation == '/':round(first/second),
    operation == '%':round(first%second)
  }
  return switch[True]

print(logo)

ans = 'y'
main_ans = float(input("Enter first number\t"))
while(ans=='y'or 'n'):  
  if ans == 'n':
    main_ans = float(input("Enter first number\t"))
  first = main_ans
  print(" + \n - \n * \n / \n % \n")
  operation = input("Pick an operation\t")
  second = float(input("What's the next number\t"))
  main_ans = switcher(first,operation,second)
  print(f"{first}\t{operation}\t{second} = {main_ans}")
  ans = input(f"Type y to continues with {main_ans} or type n to start a new calculation and to exit type anything \t")