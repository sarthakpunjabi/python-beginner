#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

def switch(choice):
  switcher = {
    10:1.10,
    12:1.12,
    15:1.15,
  }
  return switcher.get(choice,"invalid choice please try again")

print("Welcome to the tip calculator")
total_bill = int(input("What was the total bill? "))
choice = int(input("What percentage tip would you like to give? 10,12 or 15?"))
money_spliters = int(input("How many people would you like to split the bill with? "))
tip = switch(choice)
try:
  sar = round((total_bill/money_spliters)*tip,3)
  print(sar)
except:
  print("please select proper percentage in next try")