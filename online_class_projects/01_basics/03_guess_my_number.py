import random
num = int (input("till what number you want computer to generate number? "))

def guess_num(x):
  computer_guess = random.randint(1,num)
  
  guess = 0

  while guess != computer_guess:
    guess = int(input ("Guess any number: "))
    if guess >  computer_guess:
      print("OOPS!!!Too high, guess again")
    elif guess< computer_guess:
      print("OOPS!!!Too low, guess again")
  print(f"WOW!!! You Guessed Perfectly and its {computer_guess}")

guess_num(num)
