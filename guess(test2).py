secret_key="giraffe"
secret_key2="Giraffe"
guess=""
guess_count=0
guess_limit=3
out_of_chances=False
while guess!=secret_key and guess!=secret_key2 and not out_of_chances:
    if guess_count<guess_limit:
        guess_count+=1
        guess=input("Enter your guess:")
    else:
        out_of_chances=True

if out_of_chances:
    print("Out of chances,YOU LOSE")
else:
    print("You win")

