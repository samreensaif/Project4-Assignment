

while True:
  try:
    height = int(input("How tall are you? (Leave blank to stop) "))
  
    if height == "":
        break

    if height >= 50:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
  except:
    print("\nyou havent enter any height")
    break
