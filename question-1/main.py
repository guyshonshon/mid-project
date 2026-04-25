# p.s sorry for black formatting
import random
import os
from pathlib import Path

file_path = Path("file.txt")
highscore_path = Path("highscore.txt")  # least moves each line, sorted


# Utility function for redundancy (DRY)
def rand_digits(digit):
    return str(digit) * random.randrange(1, 21)


def get_user_steps(index, end_of_file_index):
    _input = input("How many characters? ")

    assert (
        _input.isdigit()
    ), f"Error, you must type a number! Current index: {index} out of {end_of_file_index}"

    return int(_input)


def get_latest_scores():
    return (
        [int(line) for line in open(highscore_path, "r")]
        if highscore_path.exists()
        else []
    )  # file closes after list population


def best_score():
    # if no scores, we need to form a single-entry list with n/a
    return (get_latest_scores() or ["N/A"])[0]


def append_score(new_score):
    latest_scores = get_latest_scores()
    latest_scores.append(new_score)
    latest_scores.sort()

    latest_10_scores = latest_scores[:10]
    with open(highscore_path, "w") as file:
        file.writelines(f"{score}\n" for score in latest_10_scores)

    return latest_10_scores


def get_eof_index(file):
    """
    while we could cheaphax "len(file.read())", for best performance
    we could seek EOF, 'tell()' and reset back cursor to the beginning.

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


# Start
print("Hidding the treasure....")


with open(
    file_path, "w"
) as file:  # w overwrites content so no need to delete pre-existing
    for digit in range(0, 10):
        file.write(rand_digits(digit))

    file.write("TREASURE")  # appends the treasure word

    for digit in range(9, -1, -1):  # reverse indexing loop
        file.write(rand_digits(digit))


# STEP 2:
with open(file_path, "r") as file:
    index = 0
    user_steps = 0
    moves = 0
    max_index = get_eof_index(file)

    print(
        f"Your best score is {best_score()} moves\nThe treasure may be found within {max_index} steps"
    )
    while True:
        direction = int(input("Where do you want to move? [1- forward 2-backwards]: "))
        moves += 1
        user_steps = get_user_steps(index, max_index)

        if direction == 1:  # backward
            if index + user_steps > max_index:
                print(f"You went too far! You can go up to {max_index - index} steps")
                continue  # let user enter input again
            index += user_steps

        elif direction == 2:  # forward
            if index - user_steps < 0:
                print(f"Too many steps, you can travel back up to {index} steps")
                continue
            index -= user_steps

        file.seek(index)
        index_char = file.read(1)

        if index_char in "TREASURE":
            print("#" * 50)
            print(f"You found the treasure '{index_char}' in {moves} attempts.")
            print("#" * 50)
            append_score(moves)
            break
        else:
            print(f"Not here... that was {index_char}! Try again! ({moves=}, {index=})")

        print("-" * 50)  # separator for ease of reading
