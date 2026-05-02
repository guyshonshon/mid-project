def get_normalized_file_name(file_name):
    """
    Return the normalized file-path for a given file-name
    """
    return f'./{file_name}'


def GetWordsFromFile(file_name):
    """
    Read file lines, then iterate through each line, split line into list of words
    and then add each word into a set, which takes care of duplications natively.
    """
    normalized_file_name = get_normalized_file_name(file_name)
    try:
        with open(normalized_file_name, 'r') as file:
            print({word for line in file.readlines() for word in line.split()})
    except FileNotFoundError:
        print(f'{normalized_file_name} does not exist')
    except PermissionError:
        print(f'Permission denied for {normalized_file_name}')


if __name__ == '__main__':
    GetWordsFromFile('test.txt')