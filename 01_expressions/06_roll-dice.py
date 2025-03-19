import random

print("Let's roll some dice!")

def roll_dice():
  die_1 = random.randint(1,6)
  die_2 = random.randint(1,6)
  return die_1,die_2

roll = roll_dice()

print (f"Die 1: {roll[0]}")
print (f"Die 2: {roll[1]}")
print (f"Total: {sum(roll)}")


