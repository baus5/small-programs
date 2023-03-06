"""Wake up, Neo...
The Matrix has you...
Follow the white rabbit.
Knock, knock, Neo."""

import sys, time, os


def main():
    clearScreen()

    # --------------
    # Raincode here!
    # --------------

    name = input("Name: ").capitalize()
    color = input("Color: ")
    animal = input("Animal: ")

    line1 = f"Wake up, {name}..."
    line2 = "The Matrix has you..."
    line3 = f"Follow the {color} {animal}."
    line4 = f"Knock, knock, {name}."

    # After inputs, clear the terminal screen.
    clearScreen()

    # Line #1 Wake up, Neo...
    slowPrint(line1, 0.1)
    clearScreen2()
    # Line #2 The Matrix has you...
    slowPrint(line2[:2], 1)  # prints "T" and waits. print "h" and waits.
    slowPrint(line2[2:], 0.1)
    clearScreen2()
    # Line #3 Follow the white rabbit.
    slowPrint(line3, 0.1)
    clearScreen2()
    # Line #4 Knock, knock, Neo.
    slowPrint(line4, 0.1)
    time.sleep(5)
    clearScreen()

    # --------------
    # Raincode here!
    # --------------


def slowPrint(line, delay):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(delay)


def clearScreen():
    """On Windows os name 'nt', 'posix' for Linux/Mac"""
    os.system("cls" if os.name == "nt" else "clear")


def clearScreen2():
    time.sleep(2)
    clearScreen()
    time.sleep(1)


# def rainCode():
#     pass


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
