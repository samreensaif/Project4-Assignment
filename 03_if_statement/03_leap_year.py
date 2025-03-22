year= int(input("Enter a year: "))


print(f"""A year is a leap year if:
It is divisible by 4, and

If it is divisible by 100, it must also be divisible by 400 to be a leap year.""")

print(f"\ndivisible by 4 = {year / 4} \ndivisible by 100 = {year / 100} \ndivisible by 400 = {year / 400}")

if (year % 4  == 0 and  year %100 !=0) or year%400==0:
  
  print("its a leap year")
else:
  print("its not a leap year")
