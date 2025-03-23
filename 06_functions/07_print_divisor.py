

def print_divisor(num:int):

  print(f"Divisors of {num}")
  print("*"*15)
  for i in range(1,num+1):
    
    if num % i == 0:
      print(i, end = " ")

def main():

  ask_num = int(input("enter number: "))
  print_divisor(ask_num)

if __name__ == "__main__":
  main()


