

import time

count_time = int(input("Enter time in seconds: "))

for i in range(count_time,0,-1):
  sec = i % 60
  min = int (i / 60) % 60
  hr = int(i / 3600)
  print (f"{hr:02}:{min:02}:{sec:02}")
  time.sleep(1)
print("times up!!!!")
