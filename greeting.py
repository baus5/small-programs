"""The Program,

..."""

import math
import os
import select  # solution ??
import sys
import time


# Program's Lines:
LINE_01 = "Welcome to the program!"
LINE_02 = "Please tell me your name?"
# Statement 2 -> Normal
LINE_05 = "Wow! You're quite fast than the others!!"
# Statement 1 -> Except
LINE_03 = "Oh! Come On! Dont be SHY!"
LINE_04 = "I am a good program..."
# Except -> Normal

# Goes Normal again.
LINE_06 = "Good to know who i am talking to!"
LINE_07 = "Nice to meet you!"
# Good-bye!
LINE_08 = "Oh no! My programmer didnt finish me yet!"
LINE_09 = "Sorry! I must go!!!"
LINE_10 = "Good Bye!"


def main():
    slowPrint(LINE_01, .05)
    time.sleep(1)
    slowPrint(LINE_02, .05)

    # Test 1:  bug for during type while counting...
    i, o, e = select.select([sys.stdin], [], [], 10)

    if (i):
        print(LINE_05, n := sys.stdin.readline().strip().upper())
    else:
        print()
        print(LINE_03)
        print(LINE_04)
        response = 'human'  # or visited...
    time.sleep(1)
    
    try:
        print(LINE_07, n)
        print(LINE_06)
    except UnboundLocalError:
        n = 'T-REX'
        time.sleep(2)
        print('ok im gonna call you', n)
        time.sleep(1)
        print(LINE_07, n)
        print(LINE_06, ';)')

    # Exit.....
    time.sleep(3)
    print(LINE_08)
    print(LINE_09)
    print(LINE_10)
    time.sleep(2)
    # input()
    clearScreen()

    # response = input("> ")
    # name = response


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def printLog():
    pass


def randomName():
    pass


def randomNick():
    pass


def slowPrint(line, delay=0.1):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clearScreen()
        sys.exit()  # When Ctrl-C is pressed, end the program.
