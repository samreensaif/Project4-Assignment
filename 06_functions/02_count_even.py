

def count_even(lst):
  print("\nEven numbers")
  print("="*10)
  
  for i in lst:
    if i%2==0:
      print(i,end=" ")




def main():
  lst=[]
  ask = input("Enter numbers: ")
  while ask != "":
    lst.append(int(ask))
    ask = input("Enter numbers: ")
  
  count_even(lst)

  

if __name__ == '__main__':
    main()

