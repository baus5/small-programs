"""Magic 8 B@ll,

More info: https://en.m.wikipedia.org/wiki/Magic_8_Ball

Tags: random, magic, luck, fortune"""

import random

answers = [
    ["It is certain."],
    ["It is decidedly so."],
    ["Without a doubt."],
    ["Yes definitely."],
    ["You may rely on it."],
    ["As I see it, yes."],
    ["Most likely."],
    ["Outlook good."],
    ["Yes."],
    ["Signs point to yes."],
    ["Reply hazy, try again."],
    ["Ask again later."],
    ["Better not tell you now."],
    ["Cannot predict now."],
    ["Concentrate and ask again."],
    ["Don't count on it."],
    ["My reply is no."],
    ["My sources say no."],
    ["Outlook not so good."],
    ["Very doubtful."],
]

while True:
    print("Ask me something...")
    response = input("> ")

    answer = random.choice(answers)
    print(answer)
    print()

    play_again = input("Shake again?").lower()
    if play_again in ("yes", "y", ""):
        continue
    else:
        break
