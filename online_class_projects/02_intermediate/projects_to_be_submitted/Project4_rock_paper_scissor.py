import random
def game():
  user=input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ")

  computer = random.choice(['r','s','p'])

  if user==computer:
    print(f"you select {user} and computer select {computer}")
    return 'tie'

  if is_win(user,computer):
    return 'you won'

  print(f"you select {user} and computer select {computer}")
  return 'you lost'

def is_win(user,computer):
  if (user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
    print(f"you select {user} and computer select {computer}")
    return True
  return False

print(game())
