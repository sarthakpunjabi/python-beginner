# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

maxi = student_scores[0]
for i in range(0,len(student_scores)-1):
  if student_scores[i]>maxi:
    maxi = student_scores[i]

print(f"{maxi} is the greatest")


