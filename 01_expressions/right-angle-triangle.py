ask_1="Enter first length of right angle triangle: "
ask_2="Enter second length of right angle triangle: "

length_1 = float(input(ask_1))
length_2 = float(input(ask_2))

def claculate_length(num1,num2):
  length_3 = (num1**2 + num2**2)**0.5
  return length_3

print(f'Length of third side: {claculate_length(length_1,length_2)}')
