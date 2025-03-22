from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
  stored_data={'samreen':'bbbbb029366f4d6b1385fc561ff3ee1a791612b579ecd8685ddce907ce8a0c9c',
               'example':'eca1dbf552edfe3038ad272d4d7f331c2a01a48eecc0e555b63f2aad9061a929'}
  
  username = input("enter username: ")
  password = input("enter password: ")
  check_password = hash_password(password)

  if username in stored_data:
   if check_password == stored_data[username]:
    print("login successful")
   else:
    print("invalid password")
  else:
    print("invalid username")

if __name__ == "__main__":
    main()

  
