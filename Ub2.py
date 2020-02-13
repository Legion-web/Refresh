#Random number guesser
def num():
    import random
    num_random = ""
    num_confirm = ""
    number = ""
    Play_again = False
    num_confirm = input("Would you like to start the game(y/n):")
    while num_confirm == "y" or num_confirm == "Y" or num_confirm == "Yes" or num_confirm == "yes" or num_confirm == "YES":
        num_random = random.randint(1,6)
        number = input("Enter a number between 1 and 6:")
        if number == str(num_random):
            print("Result = "+str(num_random))
            print("Congratulations the number you have entered matches with the random number generated,You win!")
            plagn = input("Would you like to play again (y/n)??:")
            if plagn == "y" or plagn == "Y" or plagn == "Yes" or plagn == "yes":
                play_again = True
            else:
                exit()
        else:
            print("Sorry,your guess was wrong !")
            print("The correct guess was "+str(num_random))
            plagn = input("Would you like to play again (y/n)??:")
            if plagn == "y" or plagn == "Y" or plagn == "Yes" or plagn == "yes":
                play_again = True
            else:
                exit()
    else:
        exit()
num()

num()