phonebk = {}
n=1
while True:
  ask = input("\nEnter the option:\n\n1. add a contact \n2. view phone book  \n3. delete contact \n4. Exit \n" )

  if ask == '':
    print("invalid option")
    break
  elif ask == "1":
    print("\nAdd a contact in Phone book")
    print("="*25)
    name = input (" enter name: ")
    number = input(" enter number: ")

    phonebk[name]= number
  elif ask =="2":
    print("\nPhone book")
    print("="*10)
    if not phonebk:
      print("phone book is empty")
    else:
      for i in phonebk:
        
        print(f"{n}. {i} : {phonebk[i]}")
        n += 1
  elif ask =='3':
    ask_delete = input ("enter the name u want to delte: ")

    if phonebk[ask_delete]:
      del phonebk[ask_delete]
      print(f"{ask_delete} has been deleted successfully")
    else:
      print("name not found")
  elif ask == "4":
    print("Thanks for using Phone book")
    break
  else:
    print("invalid option")
    break
  
