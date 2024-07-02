import random

n = random.randint(1,100)

user = -1
no_of_guess = 0

while(user != n):
    no_of_guess += 1
    user = int(input("Guess the number between 1 to 100: "))

    if(user > n):
        print("Lower number please!")
    elif(user < n):
        print("Higher number please!")

print(f"Congrats! You guessed the number {n} in {no_of_guess} attempts") 