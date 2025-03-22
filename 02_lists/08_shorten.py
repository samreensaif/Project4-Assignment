
def shorten(lst):
  print(lst)
  try:
    while len(lst)>=0:
      print(lst)
      lst.pop()
  except:
    print("No items found in list")


def main():
  new_lst:list=[2,3,4]
  shorten(new_lst)

if __name__ == "__main__":
    main()
