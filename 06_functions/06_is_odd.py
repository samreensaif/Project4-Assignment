

def is_num(lst):

  for i in lst:
    if i % 2 == 0:
      print (f" {i} is even", end = " ")
    else:
      print (f" {i} is odd", end = " ")

def main():
  lst=[]
  ask = int(input("enter number: "))
  while ask != "":
    lst.append(int(ask))
    ask = input("enter number: ")
    
    
  is_num(lst)

if __name__ == "__main__":
  main()
