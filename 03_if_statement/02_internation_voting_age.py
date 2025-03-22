
age = int(input ("Enter your age: "))

if age >=16 and age <= 25 :
  print("You can vote in Peturksbouipo but not in Stanlu and Mayengu")
elif age >=25 and age <= 48:
  print("You can vote in both Peturksbouipo  and Stanlau but not in Mayengu")
elif age >=48:
  print("You can vote in all three countries")
else:
  print("You can't vote in any of  three countries")
