# Guess The Number Game

This is a simple "Guess The Number" game written in Python. In this game, the program randomly selects a number between 1 and 100, and the user has to guess the number. The program provides feedback if the guess is too high or too low and counts the number of attempts.

## How to Play

1. Run the script.
2. The program will prompt you to guess a number between 1 and 100.
3. Enter your guess and press Enter.
4. The program will tell you if the number is higher or lower than your guess.
5. Keep guessing until you find the correct number.
6. The program will congratulate you and display the number of attempts you took.

## Example

```
Guess the number between 1 to 100: 50
Lower number please!
Guess the number between 1 to 100: 25
Higher number please!
Guess the number between 1 to 100: 35
Higher number please!
Guess the number between 1 to 100: 40
Lower number please!
Guess the number between 1 to 100: 38
Congrats! You guessed the number 38 in 5 attempts
```

## Requirements

- Python 3.x

## Usage

To play the game, simply run the `main.py` script:

```bash
python main.py
```

## Code

Here's the complete code for the game:

```python
import random

n = random.randint(1, 100)

user = -1
no_of_guess = 0

while user != n:
    no_of_guess += 1
    user = int(input("Guess the number between 1 to 100: "))

    if user > n:
        print("Lower number please!")
    elif user < n:
        print("Higher number please!")

print(f"Congrats! You guessed the number {n} in {no_of_guess} attempts")
```

## Contributing

If you have any ideas or improvements, feel free to submit a pull request. Contributions are always welcome!

## License

This project is licensed under the MIT License.