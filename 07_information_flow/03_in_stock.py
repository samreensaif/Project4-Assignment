
fruit = ["apple","banana","orange","grape"]

def in_stock(name:str):
  if name in fruit:
    print(f"{name} is in stock")
    if name == "apple":
      return 2
    elif name == "banana":
      return 5
    elif name == "orange":
      return 10
    elif name == "grape":
      return 15


    
  else:
    print(f"{name} is not in stock") 
    return 0

def main():
  ask = input("enter fruit name: ")
  count_stock = in_stock(ask)

  if count_stock !=0:
    print(f"Here is How many! \n {count_stock}")
  else:
    print("Sorry! the fruit is not available")


if __name__== "__main__":
  main()
