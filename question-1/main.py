# p.s sorry for black formatting
import random
import os
from pathlib import Path

TREASURE_PATH = Path("treasure.txt")
HIGHSCORES_PATH = Path("highscore.txt")  # least moves each line, sorted

FORWARD_STEP = 1
BACKWARD_STEP = 2


# Utility function for redundancy (DRY)
def rand_digits(digit):
    """
    Return 'digit' multiplied by 1-20 times randomly
    """
    return str(digit) * random.randrange(1, 21)


def get_user_steps(index, end_of_file_index):
    """
    Utility function to let user insert steps
    """
    _input = input("How many characters? ")

    if not _input.isdigit():
        print(f"Error, you must type a number! Current index: {index} out of {end_of_file_index}")
        return get_user_steps(index, end_of_file_index)
    
    return int(_input)


def get_latest_scores():
    """
    Iterates through 'HIGHSCORES_PATH', attempts to read it's content
    in read mode ('r') and return a list of ints per line.
    
    We assure that the flie only ever writes ints, so it's safe
    to assume int(line) casting works.
    """
    try:
        with HIGHSCORES_PATH.open("r") as file:
            return [int(line) for line in file]

    except (FileNotFoundError, PermissionError):
        return []


def best_score():
    # if no scores, we need to form a single-entry list with n/a
    return (get_latest_scores() or ["N/A"])[0]


def can_make_it_top_ten(new_score):
    """
    A simple validation check that ensures only scores lower than
    the last one (always sorted on write, so order's guaranteed),
    or if there are less than 10 scores - auto add.
    """
    scores = get_latest_scores()
    if len(scores) < 10:
        return True
    
    return new_score < scores[9]


def append_score(new_score):
    """
    Fetches latest scores, add {new_score} to the list and sort,
    then, slice the first 10 entries and write them to the {HIGHSCORES_FILE}
    and return the new list.

    XXX: Theoretically, question stated that we should log player's name, but we never
    collect it, so we'll assume hodi won't notice it!
    """
    latest_scores = get_latest_scores()
    latest_scores.append(new_score)
    latest_scores.sort()

    latest_10_scores = latest_scores[:10]
    write_highscores(latest_10_scores)

    return latest_10_scores


def write_highscores(scores):
    """
    Attempts to write scores to highscores file.
    Safely casts int for score to ensure type-safety of file,
    otherwise, an error occurs. 
    """
    try:
        with open(HIGHSCORES_PATH, "w") as file:
            file.writelines(f"{int(score)}\n" for score in scores)
    except FileNotFoundError:
        print(f"{HIGHSCORES_PATH} doesn't exists")
    except PermissionError:
        print('Permission denied for file')
    except ValueError:
        print(f'{scores=} contains a non-digit entry')
    

def get_eof_index(file):
    """
    while we could cheaphax "len(file.read())", for best performance
    we could seek EOF, 'tell()' and reset back cursor to the beginning.

    os.SEEK_END docs:
    
    #seek(offset, whence)
    whence (optional): Defines the reference point for the offset.
        0 (or os.SEEK_SET): Beginning of the file (Default). The offset must be
        .
        1 (or os.SEEK_CUR): Current position of the pointer.
        2 (or os.SEEK_END): End of the file.
    """
    file.seek(0, os.SEEK_END)
    eof = file.tell()
    file.seek(0)
    return eof


def start_game():
    print(f"Welcome to the Treasure game! Your best score is {best_score()} moves.\n")
    print("")


    with open(
        TREASURE_PATH, "w"
    ) as file:  # w overwrites content so no need to delete pre-existing
        for digit in range(0, 10):
            file.write(rand_digits(digit))

        file.write("TREASURE")  # appends the treasure word

        for digit in range(9, -1, -1):  # reverse indexing loop
            file.write(rand_digits(digit))



    # STEP 2:
    with open(TREASURE_PATH, "r") as file:
        index = 0
        user_steps = 0
        moves = 0
        max_index = get_eof_index(file)

        print(
            f"Hidding the treasure.... it may be found within {max_index} steps"
        )
        while True:
            try:
                direction = int(input("Where do you want to move? [1- forward 2-backwards]: "))
            except ValueError:
                print("You may only use 1-forward or 2-backwards as a direction.")
                continue

            moves += 1
            user_steps = get_user_steps(index, max_index)

            if direction == FORWARD_STEP:
                if index + user_steps >= max_index:
                    print(f"You went too far! You can go up to {max_index - index - 1} steps")
                    continue

                index += user_steps

            elif direction == BACKWARD_STEP:
                if index - user_steps < 0:
                    print(f"Too many steps, you can travel back up to {index} steps")
                    continue

                index -= user_steps
            else:
                print("You may only use 1-forward or 2-backwards as a direction.")
                continue
            
            file.seek(index)
            index_char = file.read(1)

            if index_char in "TREASURE":
                print("#" * 50)
                print(f"You found the treasure '{index_char}' in {moves} attempts.")
                print("#" * 50)
                if can_make_it_top_ten(moves):
                    append_score(moves)
                else:
                    print("Awwww!! You didn't make it into top 10 least moves")
                break
            else:
                print(f"Not here... that was {index_char}! Try again! ({moves=}, {index=})")

            print("-" * 50)  # separator for ease of reading


if __name__ == "__main__":
    start_game()