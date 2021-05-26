def ins(fname,lname):
  if len(fname)>=1 and len(lname)>=1:
    return fname.title(),lname.title()
  print("Enter in right format")
  return "we don't know","we don't know that either"


fname,lname = ins(input("Enter your first name \t"),input("Enter your last name \t"))
print(f"Your first name is {fname} and last name is {lname}")