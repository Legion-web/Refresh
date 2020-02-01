import random
emergency=False
while not(emergency):
    rndnm=random.randint(0,71)
    print(rndnm)
    if rndnm in range(7):
        emergency=True

if emergency:
    no=input("Enter a number :")
    for i in range(float(no)):
        print(i ** int(rndnm))
    else:
        print("Wrong input, Please try again ")