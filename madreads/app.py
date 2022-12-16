import club, the_matrix
import random, sys

if __name__ == "__main__":
    myChoice = random.choice([the_matrix, club])
    try:
        myChoice.main()
    except KeyboardInterrupt:
        sys.exit()
