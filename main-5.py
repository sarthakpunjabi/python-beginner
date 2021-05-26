import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

i=3
user = 0
comp = 0
print(" Select from 0 for rock 1 for paper and 2 for scissors")
choice = [rock,paper,scissors]
while(i!=0):
  user_input = int(input("Enter the choice "))
  comp_input = random.randint(0,2)
  

  if user_input >2:
    print("Invalid choice")
    i+=1
  else:
    print(choice[user_input])
    print(choice[comp_input])
    if user_input>comp_input:
      if user_input == 2 and comp_input == 0:
        print("You loose")
        comp +=1
      else:
        print("You won")
        user +=1
    elif user_input == comp_input:
      print("Tied")
      i+=1
    elif comp_input == 2 and user_input == 0:
      print("You won")
      user +=1
    else:
      print("You loose")
      comp+=1
    i -=1

if user>comp:
  print(" Over all you won")
else:
  print("Over all computer wins")







