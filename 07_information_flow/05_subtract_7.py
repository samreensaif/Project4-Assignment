

def sub_7(num:int):
  if num > 7:
    return num - 7
  else:
    return num + 5
def main():
  num = int(input("enter number: "))
  if num > 7:
    print("after subtracting 7 : ",sub_7(num))
  else:
    print("after adding 5 : ",sub_7(num))

if __name__ == "__main__":
  main()
