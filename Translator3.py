def translator():
    translate=input("Enter your phrase :")
    for letter in translate:
        if letter in "AEIOUaeiou":
            translate=translate+"g"
        else:
            translate==translate
        print(translate)
again=input("Would you like to play again ? :")
if again =="yes" or again =="Yes" or again == "Y" or again == "y":
    translator()
else:
    exit()