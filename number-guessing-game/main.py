import random

n = random.randrange(1, 10)

guess = int(input("enter a number: "))

while n!= guess:
    if guess < n:
        print("too low")
        guess = int(input("enter a number again: "))
    elif guess > n:
        print("too high!")
        guess = int(input("enter number again: "))
    else:
        break
print("you guessed it right!!")