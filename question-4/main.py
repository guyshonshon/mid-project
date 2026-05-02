import os


def get_normalized_file_name(file_name):
    """
    Return the normalized file-path for a given file-name
    """
    return f'./{file_name}'



def GetSumSize(files):
    """
    Return the sum of files in bytes.

    This function accepts a list of file names, which are iterated
    and searched on current-dir, uses `os.path.getsize()` to grab file's
    size and count towards sum.


    If file exists, add it's size to sum var,
    If file not found, print error
    If permission denied print error
    """
    sum = 0
    for file in files:
        normalized_file_name = get_normalized_file_name(file)
        try: 
            if os.path.exists(normalized_file_name):
                sum += os.path.getsize(normalized_file_name)
        except FileNotFoundError:
            print(f'{normalized_file_name} does not exist')
        except PermissionError:
            print(f'Permission denied for {normalized_file_name}')
    return sum


if __name__ == '__main__':
    print(GetSumSize(['test.txt', 'test2.txt', 'test3.txt']))
