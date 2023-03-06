import random, sys


def main():
    print("Welcome!")
    print()
    print("Simple number guessing game written with python.")
    print()

    mode = "easy"
    while True:
        print("Guess Game")
        print("> [Play]")
        print("> [Settings]")
        print("> [Exit]")
        response = input("> ").lower()

        if response in ("play", "p", ""):
            play(mode)
        elif response in ("settings", "s"):
            print("Choose game difficulty?")
            print("[easy] [normal] [hard]")

            while True:
                mode = input("> ").lower()
                if mode in ("easy", "normal", "hard"):
                    break
                else:
                    print("Please enter valid input.")
            continue  # Back to the main menu.
        elif response in ("exit", "e", "x", "q"):
            sys.exit()
        else:
            continue

        play_again = input("Play again?").lower()
        if play_again in ("yes", "y", ""):
            continue
        else:
            sys.exit()


def play(mode="easy"):
    if mode == "hard":
        upper, guessLimit = 1000, 13
    elif mode == "normal":
        upper, guessLimit = 100, 8
    else:
        upper, guessLimit = 10, 5

    isWin = False
    number = random.randint(1, upper)
    count = 0

    print(f"The number between 1 to {upper}")

    while count < guessLimit:
        guess = input("Guess the number: ")
        if not guess.isdecimal():
            print("You must enter an integer greater than 0.")
            continue
        else:
            guess = int(guess)

        if guess == number:
            print()
            print("*" * 20)
            print("***** You win! *****")
            print("*" * 20)
            isWin = True
            break
        elif guess < number:
            print("Too low")
        else:
            print("Too high")
        count += 1

    if not isWin:
        print(f"Number was {number}")
        print("Game Over!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
