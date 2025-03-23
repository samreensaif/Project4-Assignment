
def generate_sentence(word:str,num:int):
  if num == 1:
    print(f"Looking out my {word}, the sky is big and groovy!")

  elif num == 2:
    print(f"Looking out my window, the sky is big and {word}!")
  elif num == 3:
    print(f"Looking out my window, the sky is {word} and groovy! ")

def main():
  ques1= input("Enter any word : ")
  ques2= int(input(f"The word {ques1} is noun/verb/adjective? \n Choose number: \n1. Noun \n2. Verb \n3. Adjective : "))
  generate_sentence(ques1,ques2)

if __name__ == "__main__":
  main()
