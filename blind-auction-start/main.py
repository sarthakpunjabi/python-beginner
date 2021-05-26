from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to secret auction program ")
main_dict = {}
loop = 'yes'

while(loop == 'yes'):
  main_dict[input("What is your name ? ")] = int(input("What's your bid ?"))
  loop = input("Are there any biders ? type 'yes' or 'no' ")
  clear()

winner = list(main_dict.keys())[list(main_dict.values()).index(max(main_dict.values()))]
print(f"The winner is {winner} with a bid of {main_dict[winner]}")
