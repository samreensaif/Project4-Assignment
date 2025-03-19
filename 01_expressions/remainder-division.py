enter_1:int="\033[1m\033[3mEnter first number: \033[0m"
enter_2:int="\033[1m\033[3mEnter second number: \033[0m"

num_1 = int(input(enter_1))
num_2 = int(input(enter_2))

def division(num1,num2):
  division = num1//num2
  remainder = num1%num2
  return division,remainder

answer:list=division(num_1,num_2)


print(f'The Result of Division of {num_1} and {num_2} is : \033[1m\033[3m{answer[0]}\033[0m with a remainder of: \033[1m\033[3m{answer[1]}\033[0m')


