#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo,entrance,congratulations,loss

flag = 0

def check(guess,ans):
  di = {
    guess > ans : 'Too high',
    guess < ans : 'Too low',
    guess == ans : f"{congratulations} you won",
    guess >100 or guess < 0 : 'Please select in range'
  }
  return di[True]

print(entrance)
print("I'm thinking of the number between 1 to 100 ")
level = 5 if input("Choose a difficulty, Type 'easy' or 'hard' ") == 'hard' else 10 
answer = random.randint(1,100)
while(level):
  print(f"You have {level} attempts remaining to guess the number ")
  guess = int(input("Make a guess : "))
  result = check(guess,answer)
  print(result)
  level -= 1
  if 'won' in result:
    flag = 1
    break

if flag == 0:
  print(f"{loss} \n correct answer is {answer}")
