
def print_ones_digit(num:int):
  print(f"Ones digit of {num} is {num%10}")
def main():
  enter_num = int(input("Enter any number : "))
  print_ones_digit(enter_num)

if __name__ == "__main__":
  main()
