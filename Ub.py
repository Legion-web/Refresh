#String multiplier(random)
def play():
    ply=input("Would you like to run the programme(y/n) ?:")
    if ply=="y" or ply=="Y":
        util()
    else:
        exit()
def util():
    import random
    inp=""
    ext=False
    while not ext:
        inp=input("Enter a string :")
        ran_number=random.randint(1,10)
        abcd= str(inp.splitlines()) * ran_number
        print("The number generated was "+str(ran_number)+" and your result is :"+str(abcd))
        agn()
    else:
        ext = True
    if ext:
        exit()
    else:
        print("An error occured")

def agn():
    again=input("Would you like to play again ?: ")
    if again =="y" or again =="Y":
        util()
    else:
        exit()

util()
agn()
play()