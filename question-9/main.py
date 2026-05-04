SPACE = ' '


def AddWordIfNotExist(file_name, target_word):
    """
    Read file with r+ because we also need to write, then gather all words, splitted,
    check if target word does not exists in this file, if so, add it with a {SPACE} at the beginning
    for clarity.

    * after file.readlines(), cursor is now at the end of file, so it is safe to write
    with file.write(x) as it is guaranteed to be added to the end of file.
    """
    try:
        with open(file_name, 'r+') as file:
            words = (word for line in file.readlines() for word in line.split())
            if target_word not in words:
                file.write(SPACE + target_word)
                print(f'Added {target_word} because it was absent')
    except FileNotFoundError:
        print(f'{file_name} does not exist')
    except PermissionError:
        print(f'Permission denied for {file_name}')


if __name__ == '__main__':
    AddWordIfNotExist('test.txt', 'isa')