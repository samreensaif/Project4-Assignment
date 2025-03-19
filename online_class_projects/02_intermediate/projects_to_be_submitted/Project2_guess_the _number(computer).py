import random

ask=int(input("Order computer to genrate till which number: "))

def guess_num(x):
  computer_generated_number=int(random.randint(1,x))
  guess=0
  while guess!=computer_generated_number:
    guess=int(input(f"Guess a number between 1 and {x}: "))
    if guess>computer_generated_number:
      print("OOPS!!!Too high, guess again")
    elif guess<computer_generated_number:
      print("OOPS!!!Too low, guess again")

  print(f"WOW!!! You Guessed Perfectly and its {computer_generated_number}")

guess_num(ask)

