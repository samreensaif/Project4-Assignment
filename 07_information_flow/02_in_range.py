
def in_range(num,low,high):
  if num> low and num < high:
    print (f"{num} is in range between {low} and {high}")
    return True
  else:
    print (f"{num} is not in range between {low} and {high}")
    return False
def main():
  ask_num1 = int(input("enter number: "))
  ask_num2 = int(input("enter number: "))
  ask_num3 = int(input("enter number: "))
  print(in_range(ask_num1,ask_num2,ask_num3))

if __name__ == "__main__":
  main()

