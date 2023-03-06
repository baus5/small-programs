"""The 100 Prisoners Problem

The 100 prisoners problem is a mathematical problem in probability
theory and combinatorics. In this problem, 100 numbered prisoners
must find their own numbers in one of 100 drawers in order to survive.
The rules state that each prisoner may open only 50 drawers and
cannot communicate with other prisoners. At first glance, the situation
appears hopeless, but a clever strategy offers the prisoners a realistic
chance of survival. Danish computer scientist Peter Bro Miltersen first
proposed the problem in 2003.

More info at: https://en.wikipedia.org/wiki/100_prisoners_problem
Tags: math"""

import math, sys, random, copy


def main():
    info_msg = """The 100 Prisoners Problem
    
    The director of a prison offers 100 death row prisoners,
    who are numbered from 1 to 100, a last chance. A room contains a
    cupboard with 100 drawers. The director randomly puts one prisoner's
    number in each closed drawer. The prisoners enter the room, one after
    another. Each prisoner may open and look into 50 drawers in any order.
    The drawers are closed again afterwards. If, during this search, every
    prisoner finds his number in one of the drawers, all prisoners are
    pardoned. If just one prisoner does not find his number, all prisoners
    die. Before the first prisoner enters the room, the prisoners may
    discuss strategy — but may not communicate once the first prisoner enters
    to look in the drawers. What is the prisoners' best strategy?"""
    print()
    print(trim(info_msg))
    print()

    nums = list(range(1, 101))
    r_nums = copy.deepcopy(nums)
    random.shuffle(r_nums)

    prisoners = copy.deepcopy(nums)
    boxes_values = copy.deepcopy(r_nums)

    boxes_keys = copy.deepcopy(nums)
    boxes = dict(zip(boxes_keys, boxes_values))

    # Check 1 (prisoners & boxes)
    print()
    print("PRISONERS:")
    print(prisoners)
    print()
    print("BOXES")
    print(boxes)
    print()
    input("> ")

    # print('Here is all prisoners:')
    # print(prisoners)
    # print()
    # input('Press Enter to shuffle boxes')
    # print()
    # print('Shuffled Boxes:')
    # print(boxes)
    # print('Here is boxes')
    # input('> ')

    # Empty prisoner list
    prisoner_list = prisonerDictOfList("Pr", 100)
    # print(prisoner_list)
    # print()
    # input('> ')

    # Prisoner went to first box
    stepOne(prisoners, boxes, prisoner_list, "Pr")
    # print(step1)
    # print()
    # input()

    # Prisoners follow to loop
    step2 = stepTwo(prisoner_list, boxes)
    print("Their all choices:")
    print(step2)
    print()
    input()

    # goToBoxes(prisoner_list, prisoners, boxes, 'Pr')

    # Check if they found their numbers.
    step3 = stepOK(prisoner_list)
    print("Check out OK:")
    print(step3)
    print()
    input()

    # Listeyi tirmle
    step4 = stepTrim(prisoner_list)
    print("Trimmed lists")

    for k, v in step4.items():
        print(f"{k}:")
        print(v)
        print()

    # print(step4)
    print()
    input()

    # Fast check all lists.
    final = []
    for k, v in prisoner_list.items():
        if "OK" in v:
            final.append(True)
        else:
            final.append(False)
    print(final)
    print()

    # # Print out line by line:
    # for i,v in enumerate(final):
    #     print(i+1, v)

    # End of Game:
    if False not in final:
        print("All prisoners survived!")
    else:
        print("Oh boy! They failed.")

    # PLAY AGAIN
    print("Press Enter to play again or Press Q for quit")
    response = input("> ")
    if response.upper().startswith("Q"):
        sys.exit()
    else:
        main()


def prisonerDictOfList(name="list", num=100):
    """Creates multiple list dict"""
    x = list(range(1, num + 1))
    dct = {}
    for i in x:
        dct[f"{name}_%s" % i] = []
    return dct


def stepOne(p_list, b_dict, p_dict, name):
    """Add prisoners first box's num to their list."""
    for p in p_list:
        for b, n in b_dict.items():
            if p == b:
                p_dict[f"{name}_{p}"].append(n)
    return p_dict


def stepTwo(p_dict, b_dict, i=0):
    """Add rest of nums"""
    while i < 50:
        for k, v in p_dict.items():
            for j, l in b_dict.items():
                if v[i] == j:
                    p_dict[k].append(l)
        i += 1
    return p_dict


# stepOne & stepTwo
def goToBoxes(p_dict, p_list, b_dict, name, i=0):
    for p in p_list:
        for b, n in b_dict.items():
            if p == b:
                p_dict[f"{name}_{p}"].append(n)

    while i < 50:  # Because 50 choices
        for k, v in p_dict.items():
            for j, l in b_dict.items():
                if v[i] == j:
                    p_dict[k].append(l)
        i += 1

    return p_dict


def stepOK(p_dict, i=1):
    """Checks if they found their nums"""
    for k, v in p_dict.items():
        if i in v:
            x = v.index(i)
            v[x] = "OK"
            i += 1
        else:
            i += 1
    return p_dict


def stepTrim(p_dict):
    """Trims the rest of list"""
    for k, v in p_dict.items():
        if "OK" in v:
            k = v.index("OK")
            for j in range(50 - k):
                v.pop()
    return p_dict


# Loading...
def simGame(many):
    list = []
    for i in range(many):
        pass


def trim(docstring):
    """Any indentation in the first line of the docstring removed."""
    if not docstring:
        return ""
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return "\n".join(trimmed)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
