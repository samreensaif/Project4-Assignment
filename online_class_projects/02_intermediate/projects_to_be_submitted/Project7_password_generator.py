import random

print("\n\nWelcome to Password Generator!!!\n\n")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [0,1,2,3,4,5,6,7,8,9]

symbols = ["!","@","#","$","%","&","*","(",")","~"]

password=""

password_list=[]

count_letter = int(input("How Many Letters Would You Like In Your Password?\n"))
count_number = int(input("How Many Numbers Would You Like In Your Password?\n"))
count_symbol = int(input("How Many Symbols Would You Like In Your Password?\n"))

# easy password

for i in range (1,count_letter+1):
  char =random.choice(letters)
  password=password+char
  password_list +=char

for i in range (1,count_number+1):
  char =str(random.choice(numbers))
  password+=char
  password_list +=char

for i in range (1,count_symbol+1):
  char =str(random.choice(symbols))
  password+=char
  password_list +=char

print("Easy Password: ",password)

# difficult
"by using shuffle() method it changes the order of password"
random.shuffle(password_list)

# convert list into string by using ".join() method"
difficult_password = ''.join(password_list)

print("Difficult Password: ",difficult_password)


