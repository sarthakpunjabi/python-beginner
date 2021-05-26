import random
from art import logo,vs
from game_data import data
from replit import clear

print(logo)
count = 0
right = True

def selection():
  return data[random.randint(0,50)]

def comparison(com1,com2,guess):
  if com1 > com2 and guess == 'a' or com2 > com1 and guess == 'b':
    return True
  else:
    return False

compare1 = selection()

while(right):
  if count:
    print(f"You're right your current score is {count}")
  compare2 = selection()
  print(f" Compare A: {compare1['name']} , {compare1['description']}, from {compare1['country']}")
  print(vs)
  print(f" Compare B: {compare2['name']} , {compare2['description']}, from {compare2['country']}")
  guess = input("Who has more followers 'A' or 'B':").lower()
  right = comparison(int(compare1['follower_count']),int(compare2['follower_count']),guess)
  if right == False:
    print(f"Your score is {count} play next time")
  else:
    count +=1
    compare1 = compare1 if guess == 'a' else compare2
    clear()

