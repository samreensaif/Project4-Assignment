
sentence : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following sentence: " + sentence)

    user_feedback = input()  
    while user_feedback != sentence:  
        
        print("That was not the affirmation.")

        
        print("Please type the following affirmation: " + sentence)
        user_feedback = input()

    print("That's right! :)")




if __name__ == '__main__':
    main()
