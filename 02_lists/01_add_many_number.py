
# list_numbers = [2,3,4,5]

def add(*lst):
  sum = 0
  for num in lst[0]:
    sum +=num
  return sum


ask = input ("enter numbers separated by spaces: ")

list_numbers = list(map(int, ask.split()))

print(add(list_numbers))
