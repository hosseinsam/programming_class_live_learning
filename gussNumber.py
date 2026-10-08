import random


class Game:

    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 5

    def play(self):
        print("🎯 Guess the Number Game")
        print("Guess a number between 1 and 100")
        print("You have 5 attempts.\n")

        while self.attempts < self.max_attempts:

            guess = int(input("Enter your guess: "))

            self.attempts += 1

            if guess == self.secret_number:
                print("🎉 You win!")
                print("You guessed it in", self.attempts, "attempts.")
                return

            elif guess < self.secret_number:
                print("Too low!")

            else:
                print("Too high!")

            print("Attempts left:", self.max_attempts - self.attempts)
            print()

        print("💀 Game over!")
        print("The secret number was:", self.secret_number)

    def restart(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        print("\n🔄 Game restarted!\n")
        self.play()


# Create object
game = Game()

# Start game
game.play()

# Ask if player wants to restart
while True:

    answer = input("\nDo you want to play again? (yes/no): ")

    if answer.lower() == "yes":
        game.restart()

    elif answer.lower() == "no":
        print("Thanks for playing! 👋")
        break

    else:
        print("Please enter yes or no.")