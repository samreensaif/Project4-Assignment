import time
number = int(input("Enter the nummber where you want to start counting: "))

for i in range(number,0,-1):
  time.sleep(1)
  print(i)

print("Liftoff!!!")
