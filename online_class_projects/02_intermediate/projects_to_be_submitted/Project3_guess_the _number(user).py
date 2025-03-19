
import random

def computer_guess(x):
  low=1
  high=x
  response=""
  while response != 'c':
    if low!=high:
      guess = random.randint(low,high)

    else:
      guess==low

    response = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()

    if response == 'h':
      high = guess - 1
    elif response == 'l':
      low = guess + 1
  print(f'Yahoo! The computer guessed your number, {guess}, correctly!')

computer_guess(50)
