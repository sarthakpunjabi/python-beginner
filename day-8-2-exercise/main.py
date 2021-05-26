#Write your code below this line 👇
def prime_checker(number):
  flag = 0
  for i in range(2,number):
    if number%i==0:
      flag = 1

  print("It's a prime number " if flag == 0 else "It's not a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



