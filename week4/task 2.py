secret_=7
while True:
    guess=int(input("guess the number:"))
    if guess > secret_:
        print("Too High")
    elif guess < secret_:
        print("Too low")
    else:
        print("Correct")
        break


