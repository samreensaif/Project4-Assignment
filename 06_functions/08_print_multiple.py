
def print_multiple(sentence:str, num:int):
  print(sentence*num)


def main():
  ask_sentence = input("Enter a sentence: ")
  ask_num = int(input("Enter a number: "))
  print_multiple(ask_sentence, ask_num)


if __name__ == "__main__":
  main()
