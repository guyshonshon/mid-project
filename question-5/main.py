def GetWordsFromFile(file_name):
    """
    Read file lines, then iterate through each line, split line into list of words
    and then add each word into a set, which takes care of duplications natively.
    """
    try:
        with open(file_name, 'r') as file:
            print({word for line in file.readlines() for word in line.split()})
    except FileNotFoundError:
        print(f'{file_name} does not exist')
    except PermissionError:
        print(f'Permission denied for {file_name}')


if __name__ == '__main__':
    GetWordsFromFile('test.txt')