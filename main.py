import random

n = random.randint(1,100)

user = -1
no_of_guess = 0

while(user != n):
    no_of_guess += 1
    user = int(input("Guess the number between 1 to 100: "))

    if(user > n):
        print("Too large")
    elif(user < n):
        print("Too small")
        
print(f"You guessed the number {n} in {no_of_guess} attempts") 