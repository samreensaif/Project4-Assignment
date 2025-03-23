
adult_age = 18

def check_age(age:int):
  if age>=adult_age:
    print("Entered age is an adult age")
    return True
  else:
    print("Entered age is not an adult age")
    return False
def main():
  age = int(input("enter your age? "))
  print(check_age(age))

if __name__ == "__main__":
  main()
