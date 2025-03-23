

def user_data():
 ask_first_name= input("ENter first name: ")
 ask_last_name = input("Enter last name: ")
 ask_email_address = input("Enter email address: ")
 return (ask_first_name,ask_last_name,ask_email_address)
def main():
  store_user_data= user_data()
  print("\nRecieved data from user: ",store_user_data)

if __name__ == "__main__":
  main()
