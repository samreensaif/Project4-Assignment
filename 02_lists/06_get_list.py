def get_list(lst):

    print(lst)

def main():

  num_list=[]

  element=input("enter the numbers you want to save in a list ")

  while element != "":
    num_list.append(int(element))
    element=input("enter the numbers you want to save in a list or press enter to stop ")

  get_list(num_list)

if __name__ == "__main__":
    main()
