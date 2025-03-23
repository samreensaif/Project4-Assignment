
def double_num(num):
  return num*2


def main():
  ask_num = int (input("enter number: "))
  double = double_num(ask_num)
  print(f"Double of {ask_num} is {double} ")


if __name__ == '__main__':
    main()
