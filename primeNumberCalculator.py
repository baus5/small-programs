import math, sys
import random  # for testing.


def main():
    title = "Prime Number Calculator"

    print()
    print("-"*len(title))
    print("Prime Number Calculator")
    print("-"*len(title))
    print()

    print('Check if a number is prime or composite?')
    while True:
        response = input("> ")

        if response.isdecimal():
            num = int(response)
            break
        else:
            print("Please use positive non-zero integers")

    print(f"The Answer is:")
    if isPrime(num):
        print("\t", f"{num} is a prime number.")
        print(f"Only factors are: {1} and {num}")
    else:
        print("\t", f"{num} is not a prime number.")
        print(f"All factors are:")
        print("\t", ', '.join([str(factor) for factor in findFactors(num)]))


def isPrime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def findFactors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    factors = list(set(factors))
    factors.sort()
    return factors


# ----------------------------
# Simple Test
# ----------------------------
def test():
    num = random.randint(1, 999)
    print(num, isPrime(num))
    print(findFactors(num))


if __name__ == '__main__':
    try:
        # test()
        main()
    except KeyboardInterrupt:
        sys.exit()
